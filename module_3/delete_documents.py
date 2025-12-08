from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi

url = "mongodb+srv://dmitriyshirin86_db_user:password@cluster0.mfvqt3z.mongodb.net/?appName=Cluster0"

client = MongoClient(url, server_api=ServerApi('1'))

db = client.book

db.cats.delete_one({"name": "Barsik"})
result = db.cats.find_one({"name": "Barsik"})
print(result)
