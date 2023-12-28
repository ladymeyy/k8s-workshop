# Dockerfile.receiver

FROM python:3.8

WORKDIR /app

COPY receiver.py .

RUN pip install flask

CMD ["python", "receiver.py"]
