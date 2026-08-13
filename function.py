def sub(a, b):
    return a - b

def is_odd(number):
    if number % 2 != 0:
        return "it is odd number"
    else:
        return "it is even number"

def greet(name):
    return "Namaste, " + name + "!"

print(sub(5, 3))
print(is_odd(9))
print(greet("Vikas"))