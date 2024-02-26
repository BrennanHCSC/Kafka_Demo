from confluent_kafka import Consumer, KafkaError
from confluent_kafka.admin import AdminClient, NewTopic

# Configuration for connecting to Kafka
kafka_config = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'consumer-group',
    'auto.offset.reset': 'earliest'
}

# Create an AdminClient
admin_client = AdminClient({'bootstrap.servers': kafka_config['bootstrap.servers']})

# Function to check and create topic
def check_create_topic(topic_name):
    topics = admin_client.list_topics().topics
    if topic_name not in topics:
        new_topic = NewTopic(topic_name, num_partitions=1, replication_factor=1)
        admin_client.create_topics([new_topic])

# Check and create the 'nlp-topic'
check_create_topic('nlp-topic')

# Create a Consumer instance
consumer = Consumer(**kafka_config)

# Subscribe to the 'nlp-topic'
consumer.subscribe(['nlp-topic'])

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

        # Print the processed message
        print(f"Received processed message: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    print("Stopping consumer")
finally:
    # Clean up on exit
    consumer.close()
