FROM python:3.11.6-alpine
RUN apk add --update --no-cache py-pip build-base linux-headers libffi-dev

RUN mkdir /app
COPY pyproject.toml /app
COPY README.md /app
WORKDIR /app


RUN python -m pip install poetry==1.6.1 && python -m poetry check && \
    python -m poetry config virtualenvs.create false && \
    python -m poetry install --no-interaction --no-ansi --no-dev --no-root

COPY fmeaprediktor /app/fmeaprediktor
COPY main.py /app/main.py

EXPOSE 80

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "--bind", "0.0.0.0:80", "main:app"]
