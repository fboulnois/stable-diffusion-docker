#!/usr/bin/env python
import argparse, datetime, random, sys, time
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline


def isodatetime():
    return datetime.datetime.now().isoformat()


def stable_diffusion(prompt, samples, height, width, steps, scale, seed):
    model_name = "CompVis/stable-diffusion-v1-4"
    device = "cuda"

    print("load pipeline start:", isodatetime())

    with open("token.txt") as f:
        token = f.read().replace("\n", "")

    pipe = StableDiffusionPipeline.from_pretrained(model_name, use_auth_token=token).to(
        device
    )

    print("loaded models after:", isodatetime())

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

    print("loaded images after:", isodatetime())

    for i, image in enumerate(images["sample"]):
        iname = prompt.replace(" ", "_")
        image.save(
            "output/%s__steps_%d__scale_%f__seed_%d__n_%d.png"
            % (iname, steps, scale, seed, i + 1)
        )

    print("completed pipeline:", isodatetime(), flush=True)


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
        help="Unconditional guidance scale",
    )
    parser.add_argument(
        "--seed", type=int, nargs="?", default=0, help="RNG seed for repeatability"
    )
    parser.add_argument(
        "--ddim_steps", type=int, nargs="?", default=50, help="Number of sampling steps"
    )

    args = parser.parse_args()

    if args.prompt0 is not None:
        args.prompt = args.prompt0

    if args.seed == 0:
        args.seed = random.randint(1, 2**31)

    stable_diffusion(
        args.prompt,
        args.n_samples,
        args.H,
        args.W,
        args.ddim_steps,
        args.scale,
        args.seed,
    )


if __name__ == "__main__":
    main()
