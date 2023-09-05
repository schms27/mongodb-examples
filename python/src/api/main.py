from fastapi import FastAPI, HTTPException

from bson.objectid import ObjectId
from bson.json_util import loads, dumps

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from lib.mongodb_client import Client
from mapper import create_dto, create_entity

app = FastAPI()
client = Client()

@app.get("/items")
async def get_all_items():
    objects = client.listObjects()
    dto_list = list(map(create_dto, list(objects)))
    return dto_list

@app.get("/item/{item_id}")
async def get_item(item_id: str):
    document = client.getObject({'_id': ObjectId(item_id)})
    return create_dto(document)

@app.delete("/item/{item_id}")
async def delete_item(item_id: str):
    deleteCount = client.deleteObjects({'_id': ObjectId(item_id)})
    if deleteCount > 0:
        return {"ok": True}
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/item/")
async def create_item(new_item: object):
    new_id = client.writeObject(create_entity(loads(new_item)))
    return {"new_id" : new_id}

@app.put("/item/{item_id}")
async def update_item(item_id: str, updated_item: object):
    updated_count = client.updateObject({'_id': ObjectId(item_id)}, loads(updated_item))
    if updated_count > 0:
        return {"ok": True}
    raise HTTPException(status_code=404, detail="Item not found")