import pymongo
import os
from dotenv import load_dotenv
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
import gridfs
import h5py

load_dotenv()

user = os.getenv('MONGO_ROOT_USER')
password = os.getenv('MONGO_ROOT_PASSWORD')
connection_str = f"mongodb://{user}:{password}@localhost:27000"

if os.getenv("MONGO_CONNECTION_STRING") is not None:
    connection_str = os.getenv("MONGO_CONNECTION_STRING")

class Client:
    def __init__(self, verbose=False) -> None:
        self.connect()
        self.setDatabase(verbose)
        self.setCollection(verbose)

    def connect(self):
        self.client = pymongo.MongoClient(connection_str)

    def setDatabase(self, verbose, databaseName="test-database"):
        if verbose:
            print(f"Using database: {databaseName}")
        self.database = self.client[databaseName]
        self.initGridFS()

    def setCollection(self, verbose, collectionName="test-collection"):
        if verbose:
            print(f"Using collection: {collectionName}")
        self.collection = self.database[collectionName]

    def initGridFS(self):
        self.fs = gridfs.GridFS(self.database)

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
    
    def writeFile(self, data, filename=None):
        if filename is not None:
            return str(self.fs.put(data, filename=filename))
        return str(self.fs.put(data))
    
    def readFile(self, id:str):
        return self.fs.get(ObjectId(id))