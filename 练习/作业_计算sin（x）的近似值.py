import math

def sin(x,terms = 20):
    result = 0.0
    x = x%(2*math.pi)

    for n in range(terms):
        term = ((-1)**n)*(x**(2*n+1))/math.factorial(2*n+1)
        result += term

    return result

print(sin(math.pi/6))       
    
