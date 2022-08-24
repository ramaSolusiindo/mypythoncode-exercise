import sys


def add(a: int, b: int) -> int:
    return a + b


def substract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> int:
    return a / b


result = None

# Boring way
"""
try:
    if (sys.argv[1]) == 'add':
        result: int = add(20, 10)
    elif sys.argv[1] == 'substract':
        result: int = substract(20, 10)
    elif sys.argv[1] == 'multiply':
        result: int = multiply(20, 10)
    elif sys.argv[1] == 'divide':
        result: int = divide(20, 10)
    else:
        raise Exception("You entered wrong option :( ")
    print(result)
except Exception as e:
    print(str(e))
"""

# Fun Way
options = {
    'add': add,
    'substract': substract,
    'multiply': multiply,
    'divide': divide,
}
try:
    result = options[sys.argv[1]](20, 10)
    print(result)
except KeyError:
    print("You entered the wrong option :( ")
