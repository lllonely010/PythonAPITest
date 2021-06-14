from pythonapi.domain.domain_types import PetStatus

pet_add = [
    ('{"id":6600,"name":"dog6600","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"available"}', 200),
    ('{"id":6601,"name":"dog6601","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"pending"}', 200),
    ('{"id":6602,"name":"dog6602","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"sold"}', 200),
]
pet_add_ids = [f"Data=[{item[0]}], expected code={item[1]}" for item in pet_add]

pet_update = [
    ('{"id":6600,"name":"new-dog6600","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"sold"}', 200),
    ('{"id":6601,"name":"new-dog6601","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"available"}', 200),
    ('{"id":6602,"name":"new-dog6602","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"pending"}', 200),
]
pet_update_ids = [f"Data=[{item[0]}], expected code={item[1]}" for item in pet_update]

pet_id = [
    (6600, '{"id":6600,"name":"new-dog6600","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
           '"name":"string"}],"status":"sold"}', 200),
    (6601, '{"id":6601,"name":"new-dog6601","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
           '"name":"string"}],"status":"available"}', 200),
    (6602, '{"id":6602,"name":"new-dog6602","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
           '"name":"string"}],"status":"pending"}', 200),
    (999999, 'Pet not found', 404),
]
pet_id_ids = [f"Pet ID=[{item[0]}], expected code={item[2]}" for item in pet_id]

pet_status = [
    (PetStatus.available, 200),
    (PetStatus.pending, 200),
    (PetStatus.sold, 200),
]
pet_status_ids = [f"Pet status=[{item[0].value}], expected code={item[1]}" for item in pet_status]

pet_tag = [
    (['{"id":0,"name":"Tag1"}'], 200),
    (['{"id":0,"name":"Tag1"}', '{"id":22,"name":"tag2"}'], 200),
    (['{"id":10,"name":"tag11"}'], 200),
]
pet_tag_ids = [f"Pet tags=[{item[0]}], expected code={item[1]}" for item in pet_tag]

pet_upload = [
    (6600, "metadata_6600", b"binary data for upload 6600", 200),
    (6601, "metadata_6601", b"binary data for upload 6601", 200),
    (6602, "metadata_6602", b"binary data for upload 6602", 200),
]
pet_upload_ids = [f"Pet ID=[{item[0]}], expected code={item[3]}" for item in pet_upload]

pet_delete = [
    (6600, "API_KEY", 200), (6601, "API_KEY", 200), (6602, "API_KEY", 200),
]
pet_delete_ids = [f"Pet ID=[{item[0]}], expected code={item[2]}" for item in pet_delete]
