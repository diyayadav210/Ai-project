# *args
def mult(a, *nums):
    print(a)
    print(nums)
result = mult(10, 5, 5, 4)
print(result)

#**kwargs

def sub(val1 , val2, val3=5):
    return val1 - val2 - val3

result = sub(10 , 5)
result = sub(5, 10)
result = sub(val2=20 , val1=10)
result = sub(10, 5, 0)
result = sub(val1=10, val2=10, val3=10)

print(result)

def test(**kwargs):
    print(kwargs)
    return kwargs["val1"] - kwargs["val2"] - kwargs["val3"]

result = test(val1=10, val2=20, val3=40)

print(result)