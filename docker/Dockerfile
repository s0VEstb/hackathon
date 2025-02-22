FROM python:3.10-slim

WORKDIR /tur

COPY ../requirements.txt .

RUN pip install -r requirements.txt

COPY ../ .

RUN chmod +x ./docker/startup.sh
