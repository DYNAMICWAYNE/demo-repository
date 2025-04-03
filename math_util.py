def add(x,y):
    """Add two numbers and return the result """
    return x+y

def subtract(x,y):
    """Substract two numbers and return the result"""
    return x-y


def multiply(x,y):
    """Multiply two numbers and return the result"""
    return x*y

def divide(x,y):
    """Divide two numbers and return the result"""
    if y==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x/y