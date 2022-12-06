#!/usr/bin/env python
import argparse, datetime, os
import numpy as np
import torch
from PIL import Image
from torch import autocast
from diffusers import (
    OnnxStableDiffusionPipeline,
    OnnxStableDiffusionInpaintPipeline,
    OnnxStableDiffusionImg2ImgPipeline,
    StableDiffusionPipeline,
    StableDiffusionImg2ImgPipeline,
    StableDiffusionInpaintPipeline,
)


def iso_date_time():
    return datetime.datetime.now().isoformat()


def load_image(path):
    image = Image.open(os.path.join("input", path)).convert("RGB")
    print(f"loaded image from {path}:", iso_date_time(), flush=True)
    return image


def stable_diffusion_pipeline(p):
    p.dtype = torch.float16 if p.half else torch.float32

    if p.device == "cpu":
        p.diffuser = OnnxStableDiffusionPipeline
        p.revision = "onnx"
    else:
        p.diffuser = StableDiffusionPipeline
        p.revision = "fp16" if p.half else "main"

    if p.image is not None:
        if p.revision == "onnx":
            p.diffuser = OnnxStableDiffusionImg2ImgPipeline
        else:
            p.diffuser = StableDiffusionImg2ImgPipeline
        p.image = load_image(p.image)

    if p.mask is not None:
        if p.revision == "onnx":
            p.diffuser = OnnxStableDiffusionInpaintPipeline
        else:
            p.diffuser = StableDiffusionInpaintPipeline
        p.mask = load_image(p.mask)

    if p.token is None:
        with open("token.txt") as f:
            p.token = f.read().replace("\n", "")

    if p.seed == 0:
        p.seed = torch.random.seed()

    if p.revision == "onnx":
        p.seed = p.seed >> 32 if p.seed > 2**32 - 1 else p.seed
        p.generator = np.random.RandomState(p.seed)
    else:
        p.generator = torch.Generator(device=p.device).manual_seed(p.seed)

    print("load pipeline start:", iso_date_time(), flush=True)

    pipeline = p.diffuser.from_pretrained(
        p.model,
        torch_dtype=p.dtype,
        revision=p.revision,
        use_auth_token=p.token,
    ).to(p.device)

    if p.skip:
        pipeline.safety_checker = None

    if p.attention_slicing:
        pipeline.enable_attention_slicing()

    p.pipeline = pipeline

    print("loaded models after:", iso_date_time(), flush=True)

    return p


def stable_diffusion_inference(p):
    prefix = p.prompt.replace(" ", "_")[:170]
    for j in range(p.n_iter):
        with autocast(p.device):
            result = p.pipeline(
                p.prompt,
                negative_prompt=p.negative_prompt,
                init_image=p.image,
                image=p.image,
                mask_image=p.mask,
                height=p.H,
                width=p.W,
                num_images_per_prompt=p.n_samples,
                num_inference_steps=p.ddim_steps,
                guidance_scale=p.scale,
                strength=p.strength,
                generator=p.generator,
            )

        for i, img in enumerate(result.images):
            idx = j * p.n_samples + i + 1
            out = f"{prefix}__steps_{p.ddim_steps}__scale_{p.scale:.2f}__seed_{p.seed}__n_{idx}.png"
            img.save(os.path.join("output", out))

    print("completed pipeline:", iso_date_time(), flush=True)


def main():
    parser = argparse.ArgumentParser(description="Create images from a text prompt.")
    parser.add_argument(
        "prompt0",
        metavar="PROMPT",
        type=str,
        nargs="?",
        help="The prompt to render into an image",
    )
    parser.add_argument(
        "--prompt", type=str, nargs="?", help="The prompt to render into an image"
    )
    parser.add_argument(
        "--n_samples",
        type=int,
        nargs="?",
        default=1,
        help="Number of images to create per run",
    )
    parser.add_argument(
        "--n_iter",
        type=int,
        nargs="?",
        default=1,
        help="Number of times to run pipeline",
    )
    parser.add_argument(
        "--H", type=int, nargs="?", default=512, help="Image height in pixels"
    )
    parser.add_argument(
        "--W", type=int, nargs="?", default=512, help="Image width in pixels"
    )
    parser.add_argument(
        "--scale",
        type=float,
        nargs="?",
        default=7.5,
        help="Classifier free guidance scale",
    )
    parser.add_argument(
        "--seed", type=int, nargs="?", default=0, help="RNG seed for repeatability"
    )
    parser.add_argument(
        "--ddim_steps", type=int, nargs="?", default=50, help="Number of sampling steps"
    )
    parser.add_argument(
        "--attention-slicing",
        type=bool,
        nargs="?",
        const=True,
        default=False,
        help="Use less memory at the expense of inference speed",
    )
    parser.add_argument(
        "--device",
        type=str,
        nargs="?",
        default="cuda",
        help="The cpu or cuda device to use to render images",
    )
    parser.add_argument(
        "--half",
        type=bool,
        nargs="?",
        const=True,
        default=False,
        help="Use float16 (half-sized) tensors instead of float32",
    )
    parser.add_argument(
        "--image",
        type=str,
        nargs="?",
        help="The input image to use for image-to-image diffusion",
    )
    parser.add_argument(
        "--mask",
        type=str,
        nargs="?",
        help="The input mask to use for diffusion inpainting",
    )
    parser.add_argument(
        "--model",
        type=str,
        nargs="?",
        default="CompVis/stable-diffusion-v1-4",
        help="The model used to render images",
    )
    parser.add_argument(
        "--negative-prompt",
        type=str,
        nargs="?",
        help="The prompt to not render into an image",
    )
    parser.add_argument(
        "--skip",
        type=bool,
        nargs="?",
        const=True,
        default=False,
        help="Skip the safety checker",
    )
    parser.add_argument(
        "--strength",
        type=float,
        default=0.75,
        help="Diffusion strength to apply to the input image",
    )
    parser.add_argument(
        "--token", type=str, nargs="?", help="Huggingface user access token"
    )

    args = parser.parse_args()

    if args.prompt0 is not None:
        args.prompt = args.prompt0

    pipeline = stable_diffusion_pipeline(args)
    stable_diffusion_inference(pipeline)


if __name__ == "__main__":
    main()
