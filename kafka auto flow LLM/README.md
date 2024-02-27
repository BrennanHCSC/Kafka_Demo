# Kafka Python Demo

This branch automates the flow of messages from producer -> nlp -> consumer.
Producer sents messages to Kafka (which is a command-line argument by the user). Nlp modifies the message by doing a simple NLP task (reversing the message string). Consumer simply recieves messages and logs them.
Nlp and consumer are always listening.

## Getting Started

### 1. Build and Start the Docker Containers

To build and start the Docker containers, follow these steps:

- Open Visual Studio Code.
- Open the integrated terminal:
  - Press `Ctrl + `` (backtick) to open the terminal. You can also get to termina via the 'Terminal' tab at the top, followed by 'New Terminal'.
- Run the following command to build and start the containers:

```bash
docker-compose up --build -d 
```


### 2. Testing the Producer Script

Access the producer container's terminal:

- Run the following command in the terminal:

```bash
docker-compose exec producer bash
```
Inside the producer container's terminal:

- Now, you can run the producer script with a message as a command line argument. Replace <YourMessage> with the actual message you want to send:

```bash
python producer.py "<YourMessage>"
```

This will produce a message and send it to Kafka. You should see output similar to:
```mathematica
Message produced: <YourMessage> to topic test-topic [0] @ 0
Message sent to Kafka
```

- Exit the producer container
```bash
exit
```


### 3. Verifying Recieved Messages

To ensure nlp and consumer are correctly receiving and processing messages, check their logs:

- To view nlp's logs, run the following command in the terminal:

```bash
docker-compose logs nlp
```

- To view consumer's logs, run the following command in the terminal:

```bash
docker-compose logs consumer
```