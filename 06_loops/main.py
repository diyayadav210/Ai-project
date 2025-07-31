         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(10):
    print(f"{i} jaimin")

my_dict ={
    "username" : "DiyaYadav",
    "email" : "diya21@gmail.com",
    "phone_no" : 1234567890,
    "DOB" : "21-08-2005"
}

for i in my_dict:
    print(f"{i} : {my_dict[i]}")

for i in my_dict.keys():
    print(f"{i} : {my_dict[i]}")

for i in my_dict.values() :
    print(f"{i}")

for key,value in my_dict.items():
    print(f"{key} : {value}")