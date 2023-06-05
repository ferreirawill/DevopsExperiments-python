def simple_sum(a, b):
    if not is_number(a) or not is_number(b):
        raise TypeError
    return a + b


def subtract(a, b):
    if not is_number(a) or not is_number(b):
        raise TypeError
    return b - a


def multiply(a, b):
    if not is_number(a) or not is_number(b):
        raise TypeError
    return a * b


def divide(a, b):
    if not is_number(a) or not is_number(b):
        raise TypeError
    if b == 0:
        raise ZeroDivisionError
    return a / b


def power(a, b):
    if not is_number(a) or not is_number(b):
        raise TypeError
    return a ** b


def is_number(a):
    try:
        float(a)
        return True
    except ValueError:
        return False
