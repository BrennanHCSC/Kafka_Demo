FROM python:3.8-slim 

RUN pip install kafka

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app 
COPY producer.py .
RUN ["/bin/bash"]