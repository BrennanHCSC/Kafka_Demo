# Kafka Python Demo

This README guide is designed to help you quickly get started with the Kafka Python demo using Docker and Visual Studio Code.

## Getting Started

### 1. Build and Start the Docker Containers

To build and start the Docker containers, follow these steps:

- Open Visual Studio Code.
- Open the integrated terminal:
  - Press `Ctrl + `` (backtick) to open the terminal. You can also get to termina via the 'Terminal' tab at the top, followed by 'New Terminal'.
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

This will produce a message and send it to Kafka. You should see output similar to:
```mathematica
Message produced: test-topic [0] @ 0
Message sent to Kafka
```

- Run the consumer script:
```bash
python consumer.py
```

You should see output similar to:
```mathematica
Received message: Hello, World!
```

Congratulations! You've successfully produced and consumed messages using Kafka Python scripts.
