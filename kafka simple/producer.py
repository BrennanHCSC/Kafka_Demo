from confluent_kafka import Producer
import time

# Configuration for connecting to Kafka
config = {
    'bootstrap.servers': 'kafka:9092'  # Assumes Kafka is accessible at this address
}

# Create a Producer instance
producer = Producer(**config)

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message produced: {msg.topic()} [{msg.partition()}] @ {msg.offset()}")

# Produce a message
producer.produce('test-topic', 'Hello, World!', callback=acked)

# Wait for any outstanding messages to be delivered
producer.flush()

print("Message sent to Kafka")
