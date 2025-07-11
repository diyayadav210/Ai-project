#lower(), upper(), strip() = rstrip() + lstrip(), split(), join(), find(), replace(), 
# startswith(), endswith(), count(), index

first_name = "diya"
last_name = "yadav"

print(first_name + " " + last_name)
print(f"{first_name} {last_name}")

my_string = "Hello Diya , How are you?"

print(my_string, type(my_string))
print(my_string.lower())
print(my_string.upper())

username = "  diya   "
print(username, "end")
print(username.strip(), "end")
print(username.lstrip(), "end")
print(username.rstrip(), "end")

print("==========================")
print(my_string.split())
print(my_string.lower().split("d"))   # method chaing

my_string_list =['Hello', 'Diya', 'How', 'are', 'you?']
print("-".join(my_string_list))

print(my_string.find("d"))  # -1: not found
print(my_string.lower().find("d"))  #Number: index of value
print(my_string[my_string.lower().find("d")])

print(my_string.replace("Diya" , "priya"))
print(my_string.startswith("Hello"))
print(my_string.endswith("/"))

print(username.count(" "))
print(len(username))
print(username.index("d"))