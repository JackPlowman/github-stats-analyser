FROM python:3.13-alpine AS builder

WORKDIR /

COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv==0.9.0 && \
  uv export --format=requirements-txt > requirements.txt

FROM python:3.13-alpine AS analyser

WORKDIR /

RUN mkdir -p /statistics && \
  mkdir -p /cloned_repositories && \
  apk add --no-cache git=2.52.0-r0

COPY --chmod=755 run.sh run.sh
COPY analyser analyser

COPY --from=builder requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "/run.sh" ]
