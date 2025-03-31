FROM python:3.12-slim

WORKDIR /code

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r code/requirements.txt

COPY . /code

EXPOSE 8000
EXPOSE 5555
