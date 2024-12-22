# pack/divide.py
def divide(a, b):
    if b == 0:
        raise ValueError('На ноль делишь...')
    return a / b
