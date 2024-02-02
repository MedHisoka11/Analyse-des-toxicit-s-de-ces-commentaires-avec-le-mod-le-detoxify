from pymongo import MongoClient

def connect():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["instagram_data"]
    collection = db["posts"]
    return collection

def load_data_to_mongodb(data,collection):
    collection.insert_many(data)