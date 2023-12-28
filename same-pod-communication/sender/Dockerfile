FROM python:3.8

WORKDIR /app

COPY sender.py .

# Install required dependencies
RUN pip install flask requests

CMD ["python", "sender.py"]