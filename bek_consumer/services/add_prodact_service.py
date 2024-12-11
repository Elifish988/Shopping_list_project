from bek_consumer.db.mongo_db import collection


def add(product):
    collection.update_one(
        {"product_name": product["product_name"]},
        {"$set": product},  # עדכון המוצר עם הערכים החדשים
        upsert=True)  # אם לא נמצא מוצר, הוסף אותו
