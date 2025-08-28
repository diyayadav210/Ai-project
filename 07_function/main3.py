bahar_ni_value = 10

def test():
    bahar_ni_value = 20
    global_variable_dict = globals()
    print(bahar_ni_value + global_variable_dict["bahar_ni_value"])

print(bahar_ni_value)
test()
print(bahar_ni_value)
print("---------------")

def test2():
    global bahar_ni_value
    bahar_ni_value = 50
    print(bahar_ni_value)

print(bahar_ni_value)
test2()
print(bahar_ni_value)