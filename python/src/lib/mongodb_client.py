import pymongo
import os
from dotenv import load_dotenv
from bson.json_util import dumps, loads

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
        print(f"Using database: {databaseName}")
        self.database = self.client[databaseName]

    def setCollection(self, collectionName="test-collection"):
        print(f"Using collection: {collectionName}")
        self.collection = self.database[collectionName]

    def writeObject(self, object):
        data=loads(dumps(object))
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def listObjects(self):
        return loads(dumps(self.collection.find()))
    
    def getObject(self, obj_filter):
        return loads(dumps(self.collection.find_one(obj_filter)))

    def updateObject(self, obj_filter, obj):
        update_obj = {"$set":obj,"$currentDate":{"lastUpdated":True}}
        data=loads(dumps(update_obj))

        result = self.collection.update_one(obj_filter, data)
        print(f"Found '{result.matched_count}' matches, updated '{result.modified_count}'")
        return result.modified_count

    def deleteObjects(self, obj_filter):
        result = self.collection.delete_many(obj_filter)
        return result.deleted_count