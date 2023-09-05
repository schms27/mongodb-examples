import pymongo
import os
from dotenv import load_dotenv
import json

load_dotenv()

user = os.getenv('MONGO_ROOT_USER')
password = os.getenv('MONGO_ROOT_PASSWORD')

class Client:
    def __init__(self) -> None:
        self.connect()
        self.setDatabase()
        self.setCollection()

    def connect(self):
        self.client = pymongo.MongoClient(f"mongodb://{user}:{password}@localhost:27000")

    def setDatabase(self, databaseName="test-database"):
        self.database = self.client[databaseName]

    def setCollection(self, collectionName="test-collection"):
        self.collection = self.database[collectionName]

    def writeObject(self, object):
        data=json.loads(object)
        print(f"Inserting object: {data}")
        result = self.collection.insert_one(data)
        print(f"Inserted ID: {result.inserted_id}")

    def listObjects(self):
        results = self.collection.find()
        print("Found the following objects:")
        for res in results:
            print(res)

    def updateObject(self, obj_filter, object):
        update_obj = f'{{"$set":{object},"$currentDate":{{"lastUpdated":true}}}}'

        data=json.loads(update_obj)
        filter_data=json.loads(obj_filter)
        result = self.collection.update_one(filter_data, data)
        print(f"Found '{result.matched_count}' matches, updated '{result.modified_count}'")

    def deleteObjects(self, obj_filter):
        filter_data=json.loads(obj_filter)
        result = self.collection.delete_many(filter_data)
        print(f"Deleted '{result.deleted_count}' documents")