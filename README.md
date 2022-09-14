# Stable Diffusion in Docker

Runs the official [Stable Diffusion v1.4](https://huggingface.co/CompVis/stable-diffusion-v1-4)
release on [Huggingface](https://huggingface.co/) in a GPU accelerated Docker
container.

```sh
./build.sh run 'An impressionist painting of a parakeet eating spaghetti in the desert'
```

![An impressionist painting of a parakeet eating spaghetti in the desert 1](img/An_impressionist_painting_of_a_parakeet_eating_spaghetti_in_the_desert_s1.png)
![An impressionist painting of a parakeet eating spaghetti in the desert 2](img/An_impressionist_painting_of_a_parakeet_eating_spaghetti_in_the_desert_s2.png)

## Before you start

The pipeline uses the full model and weights which requires 8GB+ of GPU RAM.
On smaller GPUs you may need to modify some of the parameters. It should take a
few seconds to create one image.

Since it uses the official model, you will need to create a [user access token](https://huggingface.co/docs/hub/security-tokens)
in your [Huggingface account](https://huggingface.co/settings/tokens). Save the
user access token in a file called `token.txt` and make sure it is available
when building the container.

## Quickstart

The pipeline is managed using a single [`build.sh`](build.sh) script. You must
build the image before it can be run.

## Build

Make sure your [user access token](#before-you-start) is saved in a file called
`token.txt`. The token content should begin with `hf_...`

To build:

```sh
./build.sh build  # or just ./build.sh
```

## Run

To run:

```sh
./build.sh run 'A high tech solarpunk utopia in the Amazon rainforest'
```

### Options

Some of the options from [`txt2img.py`](https://github.com/CompVis/stable-diffusion/blob/main/scripts/txt2img.py)
are implemented for compatibility:

* `--prompt [PROMPT]`: the prompt to render into an image
* `--n_samples [N_SAMPLES]`: number of images to create per run (default 1)
* `--n_iter [N_ITER]`: number of times to run pipeline (default 1)
* `--H [H]`: image height in pixels (default 512)
* `--W [W]`: image width in pixels (default 512)
* `--scale [SCALE]`: unconditional guidance scale (default 7.5)
* `--seed [SEED]`: RNG seed for repeatability (default is a random seed)
* `--ddim_steps [DDIM_STEPS]`: number of sampling steps (default 50)

Other options:

* `--attention-slicing`: use less memory at the expense of inference speed
* `--half`: use float16 tensors instead of float32 (default float32)
* `--skip`: skip safety checker
* `--token [TOKEN]`: specify a Huggingface user access token at the command line
instead of reading it from a file

### Examples

These commands are both identical:

```sh
./build.sh run 'abstract art'
./build.sh run --prompt 'abstract art'
```

Set the seed to 42:

```sh
./build.sh run --seed 42 'abstract art'
```

Options can be combined:

```sh
./build.sh run --scale 7.0 --seed 42 'abstract art'
```

On Windows, if you aren't using WSL2 and instead use MSYS, MinGW, or Git Bash,
prefix your commands with `MSYS_NO_PATHCONV=1` (or export it beforehand):

```sh
MSYS_NO_PATHCONV=1 ./build.sh run --half --prompt 'abstract art'
```

## Outputs

### Model

The model and other files are cached in a volume called `huggingface`.

### Images

The images are saved as PNGs in the `output` folder using the prompt text. The
`build.sh` script creates and mounts this folder as a volume in the container.
