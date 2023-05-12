def func (a,b):
    if b==0:
        raise ZeroDivisionError ("You can not divide by zero")
    res=(a**2)/b
    return res
try:
    a = int(input("Enter any number: "))
    b=int(input("Enter any number: "))
    print(func(a, b))
except ValueError as h:
    print(h)
except ZeroDivisionError as k:
    print(k)
