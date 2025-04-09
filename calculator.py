import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a,b):
    if a < 0:
        raise ValueError
    return math.log(b,a)

def exp(a,b):
    return a**b







import math

def add(a, b):
    return a + b


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





