import math

def hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return round(c, 2)
    
if __name__ == '__main__':
    print(hypotenuse(3, 4))
    print(hypotenuse(10, 20))
