FROM python:3.11-slim

RUN apt-get update && apt-get install -y wget

ENV DOCKERIZE_VERSION v0.5.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

WORKDIR /app

COPY ../app /app/app
COPY ../alembic.ini /app/alembic.ini
COPY ../alembic /app/alembic
COPY ../requirements.txt /app/requirements.txt
COPY docker/start.sh /app/start.sh

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["/bin/sh", "start.sh"]
