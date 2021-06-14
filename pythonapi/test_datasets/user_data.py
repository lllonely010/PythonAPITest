user_add = [
    ('{"id":6600,"username":"user6600","firstName":"Test","lastName":"Li","email":"TestLi@email.com",'
     '"password":"6600","phone":"6600","userStatus":1}', 200),
    ('{"id":6601,"username":"user6601","firstName":"Test","lastName":"Li","email":"TestLi@email.com",'
     '"password":"6601","phone":"6601","userStatus":2}', 200),
    ('{"id":6602,"username":"user6602","firstName":"Test","lastName":"Li","email":"TestLi@email.com",'
     '"password":"6602","phone":"6602","userStatus":3}', 200),
]
user_add_ids = [f"Create user [Data: {item[0]}], expected code={item[1]}" for item in user_add]

user_login = [("user6600", "6600", 200), ("user6601", "6601", 200), ("user6602", "6602", 200), ]
user_login_ids = [f"Login with user name [{item[0]}] and password [{item[1]}], expected code={item[2]}" for item in
                  user_login]

user_delete = [
    ('user6600', 200), ('user6600', 404),
    ('user6601', 200), ('user6601', 404),
    ('user6602', 200), ('user6602', 404),
]
user_delete_ids = [f"Delete user {item[0]}], expected code={item[1]}" for item in user_delete]

user_find = [
    ('{"id":6600,"username":"user6600","firstName":"Test","lastName":"Li","email":"TestLi@email.com",'
     '"password":"6600","phone":"6600","userStatus":1}', 200),
    ('{"id":6601,"username":"user6601","firstName":"Test","lastName":"Li","email":"TestLi@email.com",'
     '"password":"6601","phone":"6601","userStatus":2}', 200),
    ('{"id":6602,"username":"user6602","firstName":"Test","lastName":"Li","email":"TestLi@email.com",'
     '"password":"6602","phone":"6602","userStatus":3}', 200),
    ('{"id":10,"username":"theUser","firstName":"Test","lastName":"Li","email":"TestLi@email.com",'
     '"password":"6600","phone":"6600","userStatus":1}', 404),
]
user_find_ids = [f"Create user [Data: {item[0]}], expected code={item[1]}" for item in user_find]

user_update = [
    ("user6600", '{"id":6600,"username":"user6600new","firstName":"Test","lastName":"Li",'
                 '"email":"TestLi@email.com","password":"6600","phone":"66000099","userStatus":1}', 200),
    ("user6601", '{"id":6601,"username":"user6601new","firstName":"Test","lastName":"Li",'
                 '"email":"TestLi@email.com","password":"6601","phone":"66010099","userStatus":2}', 200),
    ("user6602", '{"id":6602,"username":"user6602new","firstName":"Test","lastName":"Li",'
                 '"email":"TestLi@email.com","password":"6602","phone":"66020099","userStatus":3}', 200),
]
user_update_ids = [f"Update user {item[0]}], expected code={item[2]}" for item in user_update]