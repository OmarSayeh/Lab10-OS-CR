# https://github.com/OmarSayeh/Lab10-OS-CR.git
# Partner 1: Omar Sayeh
# Partner 2: Calli reiver

import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a,b):
    if a < 0:
        raise ValueError
    return math.log(b,a)

def exp(a,b):
    return a**b


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









