# Kafka Python Demo README

This README guide is designed to help you quickly get started with the Kafka Python demo using Docker and Visual Studio Code.

## Getting Started

### 1. Build and Start the Docker Containers

To build and start the Docker containers, follow these steps:

- Open Visual Studio Code.
- Open the integrated terminal:
  - Press `Ctrl + `` (backtick) to open the terminal.
- Run the following command to build the containers:

```bash
docker-compose -f .devcontainer/docker-compose.yml build
```

- Then, start the containers:

```bash
docker-compose -f .devcontainer/docker-compose.yml up -d
```

### 2. Accessing the Application Container

To access the application container's terminal:

- Run the following command in the terminal:

```bash
docker-compose -f .devcontainer/docker-compose.yml exec app bash
```


### 3. Testing Producer and Consumer Scripts

Inside the application container's terminal:

- Run the producer script:

```bash
python producer.py
```

- Run the consumer script:
```bash
python consumer.py
```
