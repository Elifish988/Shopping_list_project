import json

from kafka import  KafkaConsumer

from bek_consumer.services.add_prodact_service import add
from bek_consumer.services.del_prodact_service import deactivate_product

consumer = KafkaConsumer(
    'all.send',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    group_id='send',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    message = message.value
    print(message)
    if message['send_to'] == "add":
        product = message["product"]
        product['activ'] = True
        add(product)
        print(f"Received mail: {product}")
        consumer.commit()
    elif message['send_to'] == "del":
        product_id = message['product_id']
        deactivate_product(product_id)
        print(f"Received mail: {product_id}")
        consumer.commit()

    print(f"Received mail: {message}")

