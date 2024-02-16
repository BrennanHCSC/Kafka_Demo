# services/trigger_service/trigger_service.py

import sys
import logging
from confluent_kafka import Producer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_text(text):
    producer = Producer({'bootstrap.servers': 'kafka:9092'})
    try:
        producer.produce('nlp-requests', text.encode('utf-8'))
        producer.flush()
        logger.info(f"Sent message: {text}")
    except Exception as e:
        logger.error(f"Error sending message: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python trigger_service.py '<message>'")
    else:
        message = sys.argv[1]
        send_text(message)
