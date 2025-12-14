from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
master_db = client["master_db"]
organizations_collection = master_db["organizations"]
admins_collection = master_db["admins"]
