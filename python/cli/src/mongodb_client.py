import pymongo
import os
from dotenv import load_dotenv
import json

load_dotenv()


user = os.getenv('MONGO_ROOT_USER')
password = os.getenv('MONGO_ROOT_PASSWORD')

client = pymongo.MongoClient(f"mongodb://{user}:{password}@localhost:27000")

database = client["test-database"]

collection = database["test-collection"]

class Client:
    def writeObject(this, object):
        data=json.loads(object)
        print(f"Inserting object: {data}")
        result = collection.insert_one(data)
        print(f"Inserted ID: {result.inserted_id}")

    def listObjects(this):
        results = collection.find()
        print("Found the following objects:")
        for res in results:
            print(res)

