FROM tensorflow/tensorflow:2.11.0-gpu

RUN rm -rf /usr/local/cuda/lib64/stubs

COPY requirements.txt /

RUN pip install -r requirements.txt \
  --extra-index-url https://download.pytorch.org/whl/cu117

RUN useradd -m huggingface

USER huggingface

WORKDIR /home/huggingface

ENV USE_TORCH=1

RUN mkdir -p /home/huggingface/.cache/huggingface \
  && mkdir -p /home/huggingface/input \
  && mkdir -p /home/huggingface/output

COPY docker-entrypoint.py /usr/local/bin
COPY token.txt /home/huggingface

ENTRYPOINT [ "docker-entrypoint.py" ]
