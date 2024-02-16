# services/response_listener/response_listener.py

import logging
from confluent_kafka import Consumer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def listen_for_responses():
    consumer = Consumer({
        'bootstrap.servers': 'kafka:9092',
        'group.id': 'response-listener-service',
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': False
    })
    consumer.subscribe(['nlp-responses'])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                logger.error(f"Consumer error: {msg.error()}")
                continue

            reversed_msg = msg.value().decode('utf-8')
            print(f"Received reversed message: {reversed_msg}") 
    finally:
        consumer.close()

if __name__ == "__main__":
    listen_for_responses()
