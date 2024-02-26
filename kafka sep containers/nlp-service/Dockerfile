FROM python:3.8-slim 

RUN pip install kafka

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY nlp.py .

# Use CMD to run consumer.py automatically when the container starts
CMD ["python", "./nlp.py"]