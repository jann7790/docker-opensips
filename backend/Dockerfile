FROM python:3.9-alpine

COPY src /app
WORKDIR /app

RUN pip install -r requirements.txt


ENTRYPOINT [ "python", "server.py" ]