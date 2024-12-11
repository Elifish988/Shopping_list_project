from datetime import datetime
from bson.objectid import ObjectId

from bek_consumer.db.mongo_db import collection


def deactivate_product(product_id):
    try:
        # עדכון המסמך: 'activ' ל-false ותאריך קניה לזמן הנוכחי
        result = collection.update_one(
            {"_id": ObjectId(product_id)},
            {
                "$set": {
                    "activ": False,
                    "purchase_date": datetime.utcnow()
                }
            }
        )
        if result.matched_count == 0:
            print(f"No product found with ID: {product_id}")
        else:
            print(f"Product with ID: {product_id} was successfully deactivated.")
    except Exception as e:
        print(f"An error occurred while deactivating: {e}")

