order_place = [
    ('{"id":6600,"petId":66001,"quantity":7,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"approved",'
     '"complete":true}', 200),
    ('{"id":6601,"petId":66011,"quantity":5,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"placed",'
     '"complete":true}', 200),
    ('{"id":6602,"petId":66021,"quantity":6,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"delivered",'
     '"complete":true}', 200),
]
order_place_ids = [f"Place order [Data: {item[0]}], expected code={item[1]}" for item in order_place]

order_find = [
    ('{"id":6600,"petId":66001,"quantity":7,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"approved",'
     '"complete":true}', 200),
    ('{"id":6601,"petId":66011,"quantity":5,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"placed",'
     '"complete":true}', 404),
    ('{"id":6602,"petId":66021,"quantity":6,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"delivered",'
     '"complete":true}', 200),
    ('{"id":777777,"petId":66021,"quantity":6,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"delivered",'
     '"complete":true}', 404),
]
order_find_ids = [f"Find order [Data: {item[0]}], expected code={item[1]}" for item in order_find]

order_delete = [(6600, 200), (6601, 200), (6602, 200), (777777, 404)]
order_delete_ids = [f"Delete order [Data: {item[0]}], expected code={item[1]}" for item in order_delete]
