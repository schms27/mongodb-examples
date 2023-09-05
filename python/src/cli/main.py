import sys
import os
import argparse
from bson.json_util import dumps, loads

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from lib.mongodb_client import Client

parser = argparse.ArgumentParser(prog='main.py', description='This is a simple CLI to perform CRUD-Operations against a MongoDB instance')

parser.add_argument("command", help="the command to perform, must be one of: [write-object, list-objects, update-object, delete-objects]")
parser.add_argument("-d", "--database", help="The name of the database to use")
parser.add_argument("-c", "--collection", help="The name of the collection to use")
parser.add_argument("-o", "--object", help="The object to store or manipulate, format as JSON, ie: --object '{'this':'is a test','some':'data'}'" )
parser.add_argument("-f", "--filter", help="Used to match a certain document when updating or deleting, ie: --filter {'this':'is something else'}" )


args = parser.parse_args()

client = Client()

if args.database:
    client.setDatabase(args.database)
    client.setCollection()

if args.collection:
    client.setCollection(args.collection)

if args.command == "write-object":
    obj = {"hello":"world"}
    if args.object:
        obj = args.object
    new_id = client.writeObject(obj)
    print(f"Inserted ID: {new_id}")

elif args.command == "list-objects":
    objects = client.listObjects()
    print(f"Found the following objects: {objects}")
    json_o = dumps(list(objects))
    print(f"JSON: {json_o}")

elif args.command == "update-object":
    obj = {"hello":"world"}
    obj_filter = {};
    if args.object:
        obj = args.object
    if args.filter:
        obj_filter = args.filter
    client.updateObject(obj_filter, obj)

elif args.command == "delete-objects":
    obj_filter = {};
    if args.filter:
        obj_filter = args.filter
    deletedCount = client.deleteObjects(obj_filter)
    print(f"Deleted '{deletedCount}' documents")