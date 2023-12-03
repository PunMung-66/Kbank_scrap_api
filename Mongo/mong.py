from pymongo import MongoClient
from bson import ObjectId
from pydantic import BaseModel

client = MongoClient("mongodb+srv://admin:armageddon@userdata.ipq1o58.mongodb.net/")

class User(BaseModel):
    name: str
    username: str
    password: str

name_i = str(input())

db = client[name_i]
collection = db["users"]

collection.insert_one(User(name = name_i, username="john", password="1234").dict())
# collection.insert_one(User(name="Ben", username="Ben", password="12345").dict())