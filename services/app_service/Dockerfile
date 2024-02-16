FROM python:3.8-slim

# Set working directory
WORKDIR /workspace

# Install build tools and compilers
RUN apt-get update \
    && apt-get install -y librdkafka-dev \
    && apt-get install -y iputils-ping \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]
