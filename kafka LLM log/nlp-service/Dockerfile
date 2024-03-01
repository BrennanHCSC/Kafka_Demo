FROM python:3.8-slim 

# Install build tools and compilers
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*

RUN pip install kafka

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY nlp.py .
COPY phi-2.Q8_0.gguf .

# Use CMD to run consumer.py automatically when the container starts
CMD ["python", "./nlp.py"]