FROM python:3.9-alpine

COPY src /app
WORKDIR /app

# ARG HOST_IP
# ENV HOST_IP=${HOST_IP}

RUN pip install -r requirements.txt


ENTRYPOINT [ "python", "server.py" ]