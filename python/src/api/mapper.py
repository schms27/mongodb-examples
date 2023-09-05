from bson.objectid import ObjectId

def create_dto(entity):
    dto = entity
    id = dto.pop('_id')
    dto.pop('lastUpdated', None )
    dto['id'] = str(id)
    return dto

def create_entity(dto):
    entity = dto
    if "id" in entity:
        id = entity.pop('id')
        entity['_id'] = ObjectId(id)
    return entity