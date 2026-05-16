def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    return a**b


def square_root(n: float) -> float:
    if n < 0:
        raise ValueError("Cannot take square root of negative number")
    return n**0.5


def percentage(part: float, total: float) -> float:
    if total == 0:
        raise ValueError("Total cannot be zero")
    return (part / total) * 100
