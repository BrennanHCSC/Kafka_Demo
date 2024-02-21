from confluent_kafka import Consumer, Producer, KafkaError
import time

def reverse_string(text):
    return text[::-1]

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message produced: {msg.topic()} [{msg.partition()}] @ {msg.offset()}")

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

# Configuration for connecting to Kafka
config_prod = {
    'bootstrap.servers': 'kafka:9092'  # Assumes Kafka is accessible at this address
}

# Create a Producer instance
producer = Producer(**config_prod)

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        text = msg.value().decode('utf-8')
        reversed_mes = reverse_string(text)
        response = f"Reversed message: {reversed_mes}"
        print(response)
        producer.produce('test-topic', response.encode('utf-8'), callback=acked)
        producer.flush()
        break
finally:
    consumer.close()
    print("Message sent to Kafka")