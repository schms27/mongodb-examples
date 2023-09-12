import sys
import os
import argparse
from bson.json_util import dumps, loads

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from lib.mongodb_client import Client

parser = argparse.ArgumentParser(prog='main.py', description='This is a simple CLI to perform CRUD-Operations against a MongoDB instance')
parser.add_argument("command", help="the command to perform, must be one of: [write-object, list-objects, update-object, delete-objects, write-file, read-file, create-ts-collection]")
parser.add_argument("-d", "--database", help="The name of the database to use")
parser.add_argument("-c", "--collection", help="The name of the collection to use")
parser.add_argument("-o", "--object", help="The object to store or manipulate, format as JSON, ie: --object '{'this':'is a test','some':'data'}'" )
parser.add_argument("-f", "--filter", help="Used to match a certain document when updating or deleting, ie: --filter {'this':'is something else'}" )
parser.add_argument("-i", "--id", help="The id of the document or file to retrieve" )
parser.add_argument("-p", "--path", help="The path to the file" )
parser.add_argument("-v", "--verbose", default=False, action='store_true')
parser.add_argument("-n", "--name", help="A named argument")

args = parser.parse_args()

client = Client(args.verbose)

OUTDIR = "./tmp"

def output(value, verbose_value):
    if args.verbose:
        print(verbose_value)
    else:
        print(value)

if args.database:
    client.setDatabase(args.verbose, args.database)
    client.setCollection(args.verbose)

if args.collection:
    client.setCollection(args.verbose, args.collection)

if args.command == "write-object":
    obj = {"hello":"world"}
    if args.object:
        obj = loads(args.object)
    new_id = client.writeObject(obj)
    output(new_id, f"Inserted ID: {new_id}")

elif args.command == "write-file":
    filename = None
    if args.path:
        data = open(args.path, "rb").read()
        _, filename = os.path.split(args.path)
    elif args.object:
        data = args.object
    new_id = client.writeFile(data, filename)
    output(new_id, f"Inserted file ID: {new_id}")

elif args.command == "read-file":
    if args.id:
        file = client.readFile(args.id)
        data = file.read()
        if args.verbose:
            print(f"Got file: {file.filename}, size: {file.length}")
        if file.filename is not None:
            if not os.path.exists(OUTDIR):
                os.makedirs(OUTDIR)
            target_path = os.path.join(OUTDIR, file.filename)
            newFile = open(target_path, "wb")
            newFile.write(data)
            output(target_path, f"Saved file to: {target_path}")
        else:
            output(data, f"Data: {data}")

elif args.command == "list-objects":
    objects = client.listObjects()
    if args.verbose:
        print(f"Found the following objects: {objects}")
    json_o = dumps(list(objects))
    output(json_o, f"JSON: {json_o}")

elif args.command == "update-object":
    obj = {"hello":"world"}
    obj_filter = {};
    if args.object:
        obj = loads(args.object)
    if args.filter:
        obj_filter = loads(args.filter)
    client.updateObject(obj_filter, obj)

elif args.command == "delete-objects":
    obj_filter = {};
    if args.filter:
        obj_filter = loads(args.filter)
    deletedCount = client.deleteObjects(obj_filter)
    output(deletedCount, f"Deleted '{deletedCount}' documents")

elif args.command == "create-ts-collection":
    if args.name:
        client.createTimeseriesCollection(args.name)
    else:
        client.createTimeseriesCollection()