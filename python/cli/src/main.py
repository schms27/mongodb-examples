import argparse
from pathlib import Path
from mongodb_client import Client

parser = argparse.ArgumentParser()

parser.add_argument("command")
parser.add_argument("--object" )


# parser.add_argument("command")


args = parser.parse_args()

client = Client()

if args.command == "write-object":
    obj = {"hello":"world"}
    if args.object:
        obj = args.object
    client.writeObject(obj)
elif args.command == "list-objects":
    client.listObjects()

print(args)