import json

from kafka import KafkaProducer

from bek_consumer.db.mongo_db import collection

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))



def service_send(message):
    producer.send('all.send', value=message)
    print(f'Sent {message}')


def service_add_product(product):
    required_fields = ['product_name', 'quantity', 'user_id', 'group_id']
    missing_fields = [field for field in required_fields if field not in product]
    if missing_fields:
        return {"error": f"Missing required fields: {', '.join(missing_fields)}"}, 400
    product = {"send_to": "add" , "product" : product}
    producer.send('all.send', value=product)
    print(f"Sent {product}")
    return {"message": "Product sent successfully."}, 200



def service_del_product(product_id):
    product = {"send_to": "del", 'product_id': product_id}
    producer.send('all.send', value=product)
    print(f"Sent product_id: {product_id}")
    return {"message": "Product ID deleted successfully."}, 200


def fetch_products_by_group(group_id):
    try:
        # שליפת כל המוצרים לפי group_id
        products = list(collection.find({"group_id": group_id, "activ": True}, {"_id": 0}))  # הסרת _id מהתוצאה (אופציונלי)
        return {"products": products}, 200
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}, 500
