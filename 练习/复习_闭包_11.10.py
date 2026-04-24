def outside(a):
    b = 10
    def inner():
        nonlocal b
        print(a+b)
        b += 10
    return inner

demo = outside(20)
demo()
demo()
