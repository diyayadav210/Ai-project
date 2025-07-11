students = ["dev" , "prerita" , "gopi" , "diya"]

print(students)
print(type(students))

print(students[0] , type(students[0]) , students[0][1])
print(students[1])
print(students[2])
print(students[3])

""" we can have diff data type in single list"""

value = ["diya" , 21 , True , 99.99 ,[11 , 12 , "13" , 14, 13]]
print(value)
print(value[4])

""" this is call multi dimention indexing"""
print(value[4][2])
print(value[4][2][0])

marks1 = [11, 12, 13, 14, 15]
marks2 = [21, 22, 23, 24, 25]

""" it duplicates list by 3 """
print(marks1*3)

""" + perform concept for list and string and for int it perform multi """
print(marks1 + marks2)

print("hello"*3 + "diya")