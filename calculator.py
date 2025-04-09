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

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, base):
    if a <= 0:
        raise ValueError
    if base <= 0 or base == 1:
        raise ValueError
    return math.log(a, base)

def exp(a,b):
    return a**b


def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        return None









