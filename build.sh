#!/bin/sh

set -eu

CWD=$(basename "$PWD")

build() {
    docker build . --tag "$CWD"
}

clean() {
    docker system prune -f
}

dev() {
    docker run --rm --gpus=all --entrypoint=sh \
        -v huggingface:/home/huggingface/.cache/huggingface \
        -v "$PWD"/output:/home/huggingface/output \
        -it "$CWD"
}

run() {
    shift
    docker run --rm --gpus=all \
        -v huggingface:/home/huggingface/.cache/huggingface \
        -v "$PWD"/output:/home/huggingface/output \
        "$CWD" "$@"
}

tests() {
    docker run --rm --gpus=all \
        -v huggingface:/home/huggingface/.cache/huggingface \
        -v "$PWD"/output:/home/huggingface/output \
        "$CWD" "abstract art"
    docker run --rm --gpus=all \
        -v huggingface:/home/huggingface/.cache/huggingface \
        -v "$PWD"/output:/home/huggingface/output \
        "$CWD" --model "runwayml/stable-diffusion-v1-5" \
            --H 512 --W 512 --n_samples 2 --n_iter 2 --seed 42 \
            --scale 7.5 --ddim_steps 80 --attention-slicing \
            --half --skip --negative-prompt "red roses" \
            --prompt "bouquet of roses"
}

mkdir -p output
case ${1:-build} in
    build) build ;;
    clean) clean ;;
    dev) dev "$@" ;;
    run) run "$@" ;;
    test) tests ;;
    *) echo "$0: No command named '$1'" ;;
esac
