import argparse
from pathlib import Path
from mongodb_client import Client

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
    client.writeObject(obj)

elif args.command == "list-objects":
    client.listObjects()

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
    client.deleteObjects(obj_filter)