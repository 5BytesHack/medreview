FROM python:3.8.13-alpine3.14
ENV PYTHONUNBUFFERED 1
ENV IN_DOCKER 1

COPY requirements.txt /requirements.txt

RUN apk add --no-cache --virtual .build-deps build-base \
    && pip3 install pip --upgrade \
    && pip3 install -r /requirements.txt \
    && apk del .build-deps

EXPOSE 8001

WORKDIR /backend

ADD . /backend

VOLUME /backend

CMD python -m main