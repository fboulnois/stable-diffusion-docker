#!/bin/sh

set -eu

CWD=$(basename "$PWD")

set_gpu_arg() {
    while [ "$#" -gt 0 ]; do
        if [ "$1" = "--device" ] && [ "$2" = "cpu" ]; then
            GPU_ARG=""
            return
        fi
        shift
    done
    GPU_ARG="--gpus=all"
}

build() {
    docker build . --tag "$CWD"
}

clean() {
    docker system prune -f
}

dev() {
    docker run --rm --gpus=all --entrypoint=sh \
        -v huggingface:/home/huggingface/.cache/huggingface \
        -v "$PWD"/input:/home/huggingface/input \
        -v "$PWD"/output:/home/huggingface/output \
        -it "$CWD"
}

pull() {
    GHCR="ghcr.io/fboulnois/stable-diffusion-docker"
    docker pull "$GHCR"
    docker tag "$GHCR" "$CWD"
}

run() {
    set_gpu_arg "$@"
    docker run --rm ${GPU_ARG} \
        -v huggingface:/home/huggingface/.cache/huggingface \
        -v "$PWD"/input:/home/huggingface/input \
        -v "$PWD"/output:/home/huggingface/output \
        "$CWD" "$@"
}

tests() {
    BASE_URL="https://raw.githubusercontent.com/fboulnois/repository-assets/main/assets/stable-diffusion-docker"
    TEST_IMAGE="An_impressionist_painting_of_a_parakeet_eating_spaghetti_in_the_desert_full.png"
    curl -sL "${BASE_URL}/${TEST_IMAGE}" > "$PWD/input/${TEST_IMAGE}"
    run --half --skip --height 512 --width 640 "abstract art \\/:*?\"<>|"
    run --device cpu --onnx --image "${TEST_IMAGE}" --strength 0.6 "abstract art"
    run --model "stabilityai/stable-diffusion-2" \
        --skip --height 768 --width 768 "abstract art"
    run --model "stabilityai/stable-diffusion-2-1" \
        --skip --height 768 --width 768 "abstract art"
    run --model "stabilityai/stable-diffusion-xl-base-1.0" \
        --skip --xformers-memory-efficient-attention \
        --prompt "abstract art"
    run --model "stabilityai/stable-diffusion-x4-upscaler" \
        --image "${TEST_IMAGE}" --half --attention-slicing \
        --xformers-memory-efficient-attention \
        --prompt "An impressionist painting of a parakeet eating spaghetti in the desert"
    run --model "stabilityai/stable-diffusion-2-depth" \
        --height 768 --width 768 \
        --image "${TEST_IMAGE}" --attention-slicing \
        --xformers-memory-efficient-attention \
        --negative-prompt "bad, ugly, deformed, malformed, mutated, bad anatomy" \
        --prompt "a toucan"
    run --model "stabilityai/stable-diffusion-2-1-unclip" --image "${TEST_IMAGE}" \
        --prompt "An impressionist painting of a parakeet eating spaghetti in the desert"
    run --model "timbrooks/instruct-pix2pix" \
        --scale 7.0 --image-scale 2.0 \
        --image "${TEST_IMAGE}" --attention-slicing \
        --xformers-memory-efficient-attention \
        --negative-prompt "bad, ugly, deformed, malformed, mutated, bad anatomy" \
        --prompt "replace the sky with bricks"
    run --model "dreamlike-art/dreamlike-diffusion-1.0" \
        --skip --vae-tiling --xformers-memory-efficient-attention \
        --height 1024 --width 1024 "abstract art"
    run --model "runwayml/stable-diffusion-v1-5" \
        --samples 2 --iters 2 --seed 42 \
        --scheduler HeunDiscreteScheduler \
        --scale 7.5 --steps 80 --vae-slicing --attention-slicing \
        --half --skip --negative-prompt "red roses" \
        --prompt "bouquet of roses"
}

mkdir -p input output
case ${1:-build} in
    build) build ;;
    clean) clean ;;
    dev) dev "$@" ;;
    pull) pull ;;
    run) shift; run "$@" ;;
    test) tests ;;
    *) echo "$0: No command named '$1'" ;;
esac
