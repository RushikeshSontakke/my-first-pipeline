def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def square_root(n):
    if n < 0:
        raise ValueError("Cannot take square root of negative number")
    return n ** 0.5

def percentage(part, total):
    if total == 0:
        raise ValueError("Total cannot be zero")
    return (part / total) * 100