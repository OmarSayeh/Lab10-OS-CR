"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError as error:
        return None

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        return None




def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError

    return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if a <= 0:
        raise ValueError

    return math.log(b,a)   #use math library + raise ValueError


def exponent(a, b):
    return a**b


print(square_root(-1))



