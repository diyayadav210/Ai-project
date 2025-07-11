user_types = ("admin" , "buyer" , "seller" , "delivery" , "seller")
print(user_types)

user_count = user_types.count("seller")
print(user_count)

value = "seller"
result = -1
if value in user_types:
    result = user_types.index(value)
    print(result)

""""  how to update tuple (slice , concate)"""
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
t2 = (11, 12, 13, 14, 15, 16, 17, 18, 19)
print(t1)
print("===================")

#task 1 :remove 4 from t1
value = 4
value_index = -1
t1_updated = None
if value in t1 :
    value_index = t1.index(value)

if value_index != -1:
    t1_part1 = t1[0:value_index]
    t1_part2 = t1[value_index+1:]
    t1_updated = t1_part1 + t1_part2

print(t1_updated)

#task2 : append value
value = 9
value_index = -1
new_value = 55
t1_updated = t1 + (new_value,)

print(t1_updated)

#task3 : insert value
value = 60
insert_index = 8
t1_updated = None
if len(t1) >= insert_index :
    t1_part1 = t1[0:insert_index]
    t1_part2 = t1[insert_index:]
    t1_updated = t1_part1 + (value,) + t1_part2
print(t1_updated)
