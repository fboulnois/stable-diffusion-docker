FROM python:3.11-slim-bullseye

RUN rm -rf /usr/local/cuda/lib64/stubs

COPY requirements.txt /

RUN pip install -r requirements.txt \
  --extra-index-url https://download.pytorch.org/whl/cu118

RUN useradd -m huggingface

USER huggingface

WORKDIR /home/huggingface

ENV USE_TORCH=1

RUN mkdir -p /home/huggingface/.cache/huggingface \
  && mkdir -p /home/huggingface/input \
  && mkdir -p /home/huggingface/output

VOLUME [ "/home/huggingface/.cache/huggingface" ]
VOLUME [ "/home/huggingface/input" ]
VOLUME [ "/home/huggingface/output" ]
VOLUME [ "/tmp" ]

COPY docker-entrypoint.py /usr/local/bin
COPY token.txt /home/huggingface

ENTRYPOINT [ "docker-entrypoint.py" ]
