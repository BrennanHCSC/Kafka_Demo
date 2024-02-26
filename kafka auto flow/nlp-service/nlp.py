from confluent_kafka import Consumer, Producer, KafkaError, KafkaException, admin
from confluent_kafka.admin import AdminClient, NewTopic

# Configuration for connecting to Kafka for consuming messages
kafka_consumer_config = {
    'bootstrap.servers': 'kafka:9092',  # Assumes Kafka is accessible at this address
    'group.id': 'nlp-group',
    'auto.offset.reset': 'earliest'
}

# Producer configuration for sending processed messages
kafka_producer_config = {
    'bootstrap.servers': 'kafka:9092'
}

# Create AdminClient
admin_client = AdminClient({'bootstrap.servers': kafka_consumer_config['bootstrap.servers']})

# Function to check and create topic
def check_create_topic(topic_name):
    topics = admin_client.list_topics().topics
    if topic_name not in topics:
        new_topic = NewTopic(topic_name, num_partitions=1, replication_factor=1)
        admin_client.create_topics([new_topic])

# Check and create input and output topics
check_create_topic('test-topic')
check_create_topic('nlp-topic')

# Create a Consumer instance
consumer = Consumer(**kafka_consumer_config)

# Subscribe to the input topic
consumer.subscribe(['test-topic'])

# Create a Producer instance for sending processed messages
producer = Producer(**kafka_producer_config)

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Processed message delivered: {msg.topic()} [{msg.partition()}] @ {msg.offset()}")

try:
    while True:
        msg = consumer.poll(timeout=1.0)  # Wait for a message

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                continue
            else:
                print(msg.error())
                break

        # Decode the message
        decoded_message = msg.value().decode('utf-8')
        print(f"Received message: {decoded_message}")  # Log received message

        # Process the message (e.g., reverse the text)
        processed_message = decoded_message[::-1]

        print(f"Sending processed message: {processed_message}")  # Log message to be sent
        # Produce the processed message to the output topic
        producer.produce('nlp-topic', processed_message.encode('utf-8'), callback=acked)
        producer.flush()  # Ensure all messages are sent

except KeyboardInterrupt:
    print("Stopping NLP service")
finally:
    consumer.close()
