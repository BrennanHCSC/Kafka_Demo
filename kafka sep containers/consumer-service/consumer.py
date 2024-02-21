from confluent_kafka import Consumer, KafkaError

# Configuration for connecting to Kafka
config = {
    'bootstrap.servers': 'kafka:9092',  # Assumes Kafka is accessible at this address
    'group.id': 'test-group',
    'auto.offset.reset': 'earliest'
}

# Create a Consumer instance
consumer = Consumer(**config)

# Subscribe to the topic
consumer.subscribe(['test-topic'])

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