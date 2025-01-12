#checkov:skip=CKV_DOCKER_2
#checkov:skip=CKV_DOCKER_3
FROM python:3.13-alpine AS builder

WORKDIR /

COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry==2.0.0 && \
  pip install --no-cache-dir poetry-plugin-export==1.8.0 && \
  poetry export --output=requirements.txt

FROM python:3.13-alpine AS analyser

WORKDIR /

RUN mkdir -p /statistics && \
  mkdir -p /cloned_repositories && \
  apk add --no-cache git=2.47.1-r0

COPY --chmod=755 run.sh run.sh
COPY analyser analyser

COPY --from=builder requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "/run.sh" ]
