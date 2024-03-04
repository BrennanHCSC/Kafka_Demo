# Kafka Python Demo

This branch is the same as [kafka auto flow LLM](/kafka%20auto%20flow%20LLM/), except logs are sent to ELK.

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

- Note that the nlp container has to load/infer from the model, which may take up to 2 minutes. Consumer logs may show 'Connection refused' until inference is complete.

### 5. View the logs in Kibana

To view the logs:

- To view the logs, navigate to http://localhost:5601/
- Click 'Kibana'
- Search for 'Index Management'
- Confirm 'nlp-topic' is present in the Indices
- Click 'Index Patterns' in the left bar menu
- Create index pattern with name 'nlp-topic'
- Navigate to 'Discover' tab to see logs

### 6. Push images to Azure Container Registry

- Log in to Azure portal and "Create a resource"
- Search for "Container Registry"
- Choose subscription, resource group, and registry name; then create
- Install Azure CLI on Windows
- Log into Azure in PowerShell
- Create an alias of the docker image, tagged with the Azure CR in cmd
- Push the image to the registry in PowerShell

https://medium.com/@marvinconejo/deploying-docker-containers-on-azure-a-step-by-step-guide-to-implementing-azure-container-2dca44893dc0
https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli
https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli?tabs=azure-cli

### Architecture
![data-pipeline-new (1)](https://github.com/ron-ait/Data-pipeline/assets/100356208/cb7fd9e3-a1ad-4fbe-ad67-318cb4c55963)

### Key Components:

➣ ***Producer:*** The producer is responsible for creating the prompt and sending it to the Kafka cluster. 

➣ ***NLP:*** The NLP is responsible for consuming the prompt produced by the producer, generating a response using an LLM, and sending it to the Kafka cluster. 

➣ ***Consumer:*** The consumer is responsible for consuming the data produced by the NLP. 

➣ ***Topic:*** A topic is a category or feed name to which the records are published. Topics are used to organize the data into categories.

➣ ***Broker:*** A broker is a Kafka server that receives the records from producers and serves them to consumers. A Kafka cluster can consist of multiple brokers.

➣ ***Zookeeper:*** Zookeeper is a centralized service for maintaining configuration information and providing synchronization and coordination. In a Kafka cluster, Zookeeper helps in electing the cluster's controller and maintaining the broker and partition state.




