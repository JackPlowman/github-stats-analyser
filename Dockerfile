FROM python:3.14-alpine AS builder

WORKDIR /

COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv==0.13.5 && \
  uv export --frozen --no-dev --no-emit-project --format=requirements-txt > requirements.txt

FROM python:3.14-alpine AS analyser

WORKDIR /

RUN mkdir -p /statistics && \
  mkdir -p /cloned_repositories && \
  apk add --no-cache git

COPY --chmod=755 run.sh run.sh
COPY analyser analyser

COPY --from=builder requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "/run.sh" ]
