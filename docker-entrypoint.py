#!/usr/bin/env python
import argparse, datetime, random, time
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline


def cuda_device():
    return "cuda"


def iso_date_time():
    return datetime.datetime.now().isoformat()


def skip_safety_checker(images, *args, **kwargs):
    return images, False


def stable_diffusion_pipeline(model, half, skip, do_slice, token):
    if token is None:
        with open("token.txt") as f:
            token = f.read().replace("\n", "")

    dtype, rev = (torch.float16, "fp16") if half else (torch.float32, "main")

    print("load pipeline start:", iso_date_time())

    pipeline = StableDiffusionPipeline.from_pretrained(
        model, torch_dtype=dtype, revision=rev, use_auth_token=token
    ).to(cuda_device())

    if skip:
        pipeline.safety_checker = skip_safety_checker

    if do_slice:
        pipeline.enable_attention_slicing()

    print("loaded models after:", iso_date_time())

    return pipeline


def stable_diffusion_inference(
    pipeline, prompt, neg_prompt, samples, iters, height, width, steps, scale, seed
):
    if seed == 0:
        seed = torch.random.seed()

    prefix = prompt.replace(" ", "_")[:170]

    generator = torch.Generator(device=cuda_device()).manual_seed(seed)
    for j in range(iters):
        with autocast(cuda_device()):
            result = pipeline(
                prompt,
                negative_prompt=neg_prompt,
                height=height,
                width=width,
                num_images_per_prompt=samples,
                num_inference_steps=steps,
                guidance_scale=scale,
                generator=generator,
            )

        for i, image in enumerate(result.images):
            image.save(
                "output/%s__steps_%d__scale_%0.2f__seed_%d__n_%d.png"
                % (prefix, steps, scale, seed, j * samples + i + 1)
            )

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
        "--half",
        type=bool,
        nargs="?",
        const=True,
        default=False,
        help="Use float16 (half-sized) tensors instead of float32",
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
        "--token", type=str, nargs="?", help="Huggingface user access token"
    )

    args = parser.parse_args()

    if args.prompt0 is not None:
        args.prompt = args.prompt0

    pipeline = stable_diffusion_pipeline(
        args.model, args.half, args.skip, args.attention_slicing, args.token
    )

    stable_diffusion_inference(
        pipeline,
        args.prompt,
        args.negative_prompt,
        args.n_samples,
        args.n_iter,
        args.H,
        args.W,
        args.ddim_steps,
        args.scale,
        args.seed,
    )


if __name__ == "__main__":
    main()
