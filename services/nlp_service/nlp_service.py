from confluent_kafka import Consumer, Producer, KafkaError

def reverse_string(text):
    return text[::-1]

# Kafka Consumer for incoming text messages
consumer = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'nlp-service',
    'auto.offset.reset': 'earliest'
})

# Kafka Producer for sending back the letter count
producer = Producer({'bootstrap.servers': 'kafka:9092'})

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")

consumer.subscribe(['nlp-requests'])

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
        producer.produce('nlp-responses', response.encode('utf-8'), callback=acked)
        producer.flush()
finally:
    consumer.close()
