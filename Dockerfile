FROM python:3.12-alpine

WORKDIR /code

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apk update \
    && apk upgrade -a \
    && rm -rf /var/cache/apk/*

COPY ./requirements.txt code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r code/requirements.txt

COPY . /code

EXPOSE 8000
EXPOSE 5555
