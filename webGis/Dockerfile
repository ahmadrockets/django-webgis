FROM python:3.6.9-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add --no-cache mariadb-dev
RUN pip install -r requirements.txt
COPY . /app