def addition(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divider(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0
