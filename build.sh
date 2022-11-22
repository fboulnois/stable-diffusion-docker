#!/bin/sh

set -eu

CWD=$(basename "$PWD")

set_gpu_arg() {
    while [ "$#" -gt 0 ]; do
        if [ "$1" = "--device" ] && [ "$2" = "cpu" ]; then
            GPU_ARG=""
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

run() {
    set_gpu_arg "$@"
    docker run --rm ${GPU_ARG} \
        -v huggingface:/home/huggingface/.cache/huggingface \
        -v "$PWD"/input:/home/huggingface/input \
        -v "$PWD"/output:/home/huggingface/output \
        "$CWD" "$@"
}

tests() {
    TEST_IMAGE="An_impressionist_painting_of_a_parakeet_eating_spaghetti_in_the_desert_s1.png"
    cp "img/${TEST_IMAGE}" "input/${TEST_IMAGE}"
    run --H 512 --W 640 "abstract art"
    run --device cpu --image "${TEST_IMAGE}" --strength 0.6 "abstract art"
    run --model "runwayml/stable-diffusion-v1-5" \
        --n_samples 2 --n_iter 2 --seed 42 \
        --scale 7.5 --ddim_steps 80 --attention-slicing \
        --half --skip --negative-prompt "red roses" \
        --prompt "bouquet of roses"
}

mkdir -p input output
case ${1:-build} in
    build) build ;;
    clean) clean ;;
    dev) dev "$@" ;;
    run) shift; run "$@" ;;
    test) tests ;;
    *) echo "$0: No command named '$1'" ;;
esac
