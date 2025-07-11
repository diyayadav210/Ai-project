user1 = ["diya", 20, 1234567890, "diya_210", "21-08-2005", "diya@21"]
user2 = ["jaimin", "asdf@1234", 25, 2135467890, "mrjemmy", "14-11-xxxx"]

user1 = {
    "name" : "diya",
    "age" : 20,
    "phone_no" : 1234567890,
    "DOB" : "21-08-2005",
    "password" : "diya@21",
    "username" : "diya_210"
}

user2 = {
    "name" : "jaimin",
    "age" : 25,
    "phone_no" : 2135467890,
    "DOB" : "14-11-xxxx",
    "password" : "asdf@1234",
    "username" : "mrjemmy"
}

print(user1)
print(user1["name"])
print(user1["username"])
print(user2)
print(user2["name"])
print(user2["username"])