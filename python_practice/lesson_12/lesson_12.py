with open("example.txt") as f: #менеджер контексту
    print(f.read())

try:
    f = open("example.txt") # __enter__
    print(f.read())
finally:
    f.close() #__exit__

print("Function for adding some numbers")
def some_function(a, b):
    print(a+b)
    return a + b

def factorial(n):
    if n < 0:
        raise ValueError(f"You have to use 0 or positive numbers. You put {n}")

    if type(n) != int:
        raise TypeError(f"You have to use int. You put {n}")

    if n == 0:
        return 1

    else:
        return f"else result"

