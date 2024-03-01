from faker import Faker
from kafka import KafkaProducer
import json 
import time 

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer= lambda x: json.dumps(x).encode('utf-8')
)


fake = Faker()
i =0
while i < 10:
    message= {
        'name':fake.name(),
        'city':fake.city(),
        'phone':fake.phone_number()
        }
    key = 'message_update'.encode('utf-8')


    producer.send(
        topic='new-updates',
        key=key,
        value=message
    )
    time.sleep(1)
    i=i+1

