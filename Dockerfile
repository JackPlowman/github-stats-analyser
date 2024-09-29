#checkov:skip=CKV_DOCKER_2
#checkov:skip=CKV_DOCKER_3
FROM python:3.12-alpine

WORKDIR /

RUN mkdir -p /statistics && \
  apk add git=2.45.2-r0

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry==1.8.3 \
  && poetry install --no-dev

COPY analyser ./analyser

CMD [ "poetry", "run", "python", "-m", "analyser" ]