import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take sqrt of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b



def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Denominator (a) cannot be 0")
    return b / a



def exp(a, b):
    return a ** b




def subtract(a, b):
    return a - b



def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm")
    return math.log(b, a)



