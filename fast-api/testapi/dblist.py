from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:November@userdata.ipq1o58.mongodb.net/")
dbs = client.list_database_names()

print(dbs)
