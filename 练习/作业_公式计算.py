import math 
def f(x):
    y = math.pi * math.e ** math.sin(x) + math.log(abs(math.cos(x))) + math.tan(x)
    return y

print(f(math.pi))
