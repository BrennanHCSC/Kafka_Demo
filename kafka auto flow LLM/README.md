# Kafka Python Demo

This branch is the same as [kafka auto flow](/kafka%20auto%20flow/), except instead of a simple nlp task, an LLM model is subbed in.

## Getting Started

### 1. Downloading LLM Model File

To download and correctly place the model file:
- Go to [this link](https://huggingface.co/TheBloke/phi-2-GGUF/blob/main/phi-2.Q8_0.gguf) and download the model file 'phi-2.Q8_0.gguf'.
- Put the file into [nlp-service/](nlp-service/) directory.




### 2. Build and Start the Docker Containers

To build and start the Docker containers, follow these steps:

- Open Visual Studio Code.
- Open the integrated terminal:
  - Press `Ctrl + `` (backtick) to open the terminal. You can also get to termina via the 'Terminal' tab at the top, followed by 'New Terminal'.
- Run the following command to build and start the containers:

```bash
docker-compose up --build -d 
```

### 3. Testing the Producer Script

Access the producer container's terminal:

- Run the following command in the terminal:

```bash
docker-compose exec producer bash
```
Inside the producer container's terminal:

- Now, you can run the producer script with an LLM as a command line argument. Replace <YourPrompt> with the actual prompt you want to send:

```bash
python producer.py "<YourPrompt>"
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


### 4. Viewing Model Output

To view the output of the model, view consumer's logs:

- To view consumer's logs, run the following command in the terminal:

```bash
docker-compose logs consumer
```