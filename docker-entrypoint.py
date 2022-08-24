#!/usr/bin/env python
import datetime, random, sys, time
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline


def isodatetime():
    return datetime.datetime.now().isoformat()


def stable_diffusion(prompt):
    model_name = "CompVis/stable-diffusion-v1-4"
    device = "cuda"

    print("load pipeline start:", isodatetime())

    with open("token.txt") as f:
        token = f.read().replace("\n", "")

    pipe = StableDiffusionPipeline.from_pretrained(model_name, use_auth_token=token).to(
        device
    )

    print("loaded models after:", isodatetime())

    samples = 1
    steps = 40
    scale = 7
    seed = random.randint(1, 2**31)
    generator = torch.Generator(device=device).manual_seed(seed)
    with autocast(device):
        images = pipe(
            prompt * samples,
            num_inference_steps=steps,
            guidance_scale=scale,
            generator=generator,
        )

    print("loaded images after:", isodatetime())

    for i, image in enumerate(images["sample"]):
        iname = prompt[0].replace(" ", "_")
        image.save("output/%s__steps_%d__scale_%d__seed_%d__n_%d.png" % (iname, steps, scale, seed, i + 1))

    print("completed pipeline:", isodatetime(), flush=True)


stable_diffusion(sys.argv[1:])
