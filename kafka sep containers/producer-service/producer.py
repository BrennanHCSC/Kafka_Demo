from confluent_kafka import Producer
import time
import sys  # Import the sys module to access command line arguments

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

# Check if a message is provided as a command line argument
if len(sys.argv) > 1:
    message = sys.argv[1]
else:
    print("No message provided, defaulting to 'Hello, World!'")
    message = "Hello, World!"

# Produce a message using the command line argument or default message
producer.produce('test-topic', message, callback=acked)

# Wait for any outstanding messages to be delivered
producer.flush()

print("Message sent to Kafka")
