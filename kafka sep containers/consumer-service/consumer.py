from confluent_kafka import Consumer, KafkaError, KafkaException
from confluent_kafka.admin import AdminClient, NewTopic

# Configuration for connecting to Kafka
kafka_config = {
    'bootstrap.servers': 'kafka:9092',  # Assumes Kafka is accessible at this address
    'group.id': 'test-group',
    'auto.offset.reset': 'earliest'
}

# Create an AdminClient
admin_client = AdminClient({'bootstrap.servers': kafka_config['bootstrap.servers']})

# Define the topic to be created
topic_name = 'test-topic'
topic_config = {
    'num_partitions': 1,
    'replication_factor': 1
}

# Check if the topic exists
metadata = admin_client.list_topics(timeout=10)
if topic_name not in metadata.topics:
    # Topic doesn't exist, so create it
    topic = NewTopic(topic_name, **topic_config)
    fs = admin_client.create_topics([topic])

    # Block until the topic is created
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print(f"Topic {topic} created")
        except Exception as e:
            print(f"Failed to create topic {topic}: {e}")

# Create a Consumer instance
consumer = Consumer(**kafka_config)

# Subscribe to the topic
consumer.subscribe([topic_name])

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

        print(f"Received message: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    print("Stopping consumer")
finally:
    # Clean up on exit
    consumer.close()
