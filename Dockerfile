FROM tensorflow/tensorflow:2.10.0-gpu

COPY requirements.txt /

RUN pip install -r requirements.txt \
  --extra-index-url https://download.pytorch.org/whl/cu116

RUN useradd -m huggingface

USER huggingface

WORKDIR /home/huggingface

RUN mkdir -p /home/huggingface/.cache/huggingface \
  && mkdir -p /home/huggingface/output

COPY docker-entrypoint.py /usr/local/bin
COPY token.txt /home/huggingface

ENTRYPOINT [ "docker-entrypoint.py" ]
