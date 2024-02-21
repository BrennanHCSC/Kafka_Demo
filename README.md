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

### 2. Testing the Producer Script

Access the producer container's terminal:

- Run the following command in the terminal:

```bash
docker-compose -f .devcontainer/docker-compose.yml exec producer bash
```
Inside the producer container's terminal:

- Run the producer script:

```bash
python producer.py
```

This will produce a message and send it to Kafka. You should see output similar to:
```mathematica
Message produced: test-topic [0] @ 0
Message sent to Kafka
```

- Exit the producer container
```bash
exit
```

### 3. Testing NLP Script

Access the NLP container's terminal:

- Run the following command in the terminal:

```bash
docker-compose -f .devcontainer/docker-compose.yml exec nlp bash
```
Inside the NLP container's terminal:

- Run the NLP script:

```bash
python nlp.py
```

This will produce a message and send it to Kafka. You should see output similar to:
```mathematica
Reversed message: !dlroW ,olleH
Message produced: test-topic [0] @ 0
Message sent to Kafka
```

- Exit the NLP container
```bash
exit
```

### 4. Testing Consumer Script

Access the consumer container's terminal:

- Run the following command in the terminal:

```bash
docker-compose -f .devcontainer/docker-compose.yml exec consumer bash
```
Inside the consumer container's terminal:

- Run the consumer script:

```bash
python consumer.py
```

You should see output similar to:
```mathematica
Received message: Reversed message: !dlroW ,olleH
```

Congratulations! You've successfully produced and consumed messages using Kafka Python scripts.
