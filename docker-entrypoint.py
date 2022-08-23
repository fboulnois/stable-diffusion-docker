#!/usr/bin/env python
import datetime, sys, time
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
from PIL import Image


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
    generator = torch.Generator(device=device).manual_seed(42)
    with autocast(device):
        images = pipe(
            prompt * samples,
            num_inference_steps=steps,
            guidance_scale=scale,
            generator=generator,
        )

    print("loaded images after:", isodatetime())

    i = 1
    for image in images["sample"]:
        iname = prompt[0].replace(" ", "_")
        image.save("output/%s_%d.png" % (iname, i))
        i = i + 1

    print("completed pipeline:", isodatetime(), flush=True)


stable_diffusion(sys.argv[1:])
