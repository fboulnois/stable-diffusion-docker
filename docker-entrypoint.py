#!/usr/bin/env python
import argparse, datetime, random, time
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline


def iso_date_time():
    return datetime.datetime.now().isoformat()


def skip_safety_checker(images, *args, **kwargs):
    return images, False


def stable_diffusion(prompt, samples, height, width, steps, scale, seed, half, skip):
    model_name = "CompVis/stable-diffusion-v1-4"
    device = "cuda"

    dtype, rev = (torch.float16, "fp16") if half else (torch.float32, "main")

    print("load pipeline start:", iso_date_time())

    with open("token.txt") as f:
        token = f.read().replace("\n", "")

    pipe = StableDiffusionPipeline.from_pretrained(
        model_name, torch_dtype=dtype, revision=rev, use_auth_token=token
    ).to(device)

    if skip:
        pipe.safety_checker = skip_safety_checker

    print("loaded models after:", iso_date_time())

    generator = torch.Generator(device=device).manual_seed(seed)
    with autocast(device):
        images = pipe(
            [prompt] * samples,
            height=height,
            width=width,
            num_inference_steps=steps,
            guidance_scale=scale,
            generator=generator,
        )

    print("loaded images after:", iso_date_time())

    for i, image in enumerate(images["sample"]):
        iname = prompt.replace(" ", "_")[:170]
        image.save(
            "output/%s__steps_%d__scale_%0.2f__seed_%d__n_%d.png"
            % (iname, steps, scale, seed, i + 1)
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
        "--n_samples", type=int, nargs="?", default=1, help="Number of images to create"
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
        "--half",
        type=bool,
        nargs="?",
        const=True,
        default=False,
        help="Use float16 (half-sized) tensors instead of float32",
    )
    parser.add_argument(
        "--skip",
        type=bool,
        nargs="?",
        const=True,
        default=False,
        help="Skip the safety checker",
    )

    args = parser.parse_args()

    if args.prompt0 is not None:
        args.prompt = args.prompt0

    if args.seed == 0:
        args.seed = torch.random.seed()

    stable_diffusion(
        args.prompt,
        args.n_samples,
        args.H,
        args.W,
        args.ddim_steps,
        args.scale,
        args.seed,
        args.half,
        args.skip,
    )


if __name__ == "__main__":
    main()
