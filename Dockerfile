FROM python:3.10.12-slim-buster

WORKDIR /app
COPY . /app

EXPOSE 8000

RUN apt-get update \
&& apt-get install -y pkg-config \
&& apt-get install -y gcc \
&& apt-get install -y default-libmysqlclient-dev \
&& apt-get install -y python3-dev

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt