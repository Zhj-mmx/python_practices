def f(x):
    return x**2

ls = [1,2,3,4,5,6,7,8,9]
list = (map(f,ls))
for i in range(10):
    print(next(list))
