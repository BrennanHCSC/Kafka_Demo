# Kafka Python Demo README

This README guide is designed to help you get started with the Kafka Python demo. This demo includes basic examples of a Kafka producer and consumer written in Python, utilizing the Confluent Kafka library. The setup is containerized using Docker, making it easy to run and manage the Kafka environment.

## Prerequisites

Before you start, ensure you have the following installed on your system:
- Docker
- Docker Compose
- (Optional) Visual Studio Code with Remote - Containers extension for development

## Getting Started

Follow these steps to get your Kafka Python demo up and running:

### 1. Clone the Repository

First, clone the repository containing the demo to your local machine. Open your terminal and run:

```bash
git clone <repository-url>
cd <repository-directory>
```

Replace `<repository-url>` with the actual URL of the repository and `<repository-directory>` with the name of the directory that Git clones.

### 2. Build and Run the Docker Containers

Run the following command to build and start the Docker containers using Docker Compose from the root of the project directory:

```bash
docker-compose -f .devcontainer/docker-compose.yml up --build
```

This command will start the Kafka broker, Zookeeper, and your application container. The application container is set up with all the necessary dependencies installed.

### 3. Accessing the Jupyter Notebook (Optional)

If you plan to use Jupyter notebooks for interactive development:

- After the containers are up, navigate to `http://localhost:8888` on your web browser.
- You might need a token to access the Jupyter notebook. Check the terminal logs of the Jupyter container for a URL containing the token.

### 4. Running the Producer and Consumer Scripts

To run the producer and consumer Python scripts, you need to access the terminal of the application container. You can do this in several ways, but if you're using Docker directly, you can use:

```bash
docker exec -it <container_name> /bin/bash
```

Replace `<container_name>` with the name of your application container. Once inside the container:

To run the producer script:

```bash
python producer.py
```

To run the consumer script in another terminal session:

```bash
python consumer.py
```
