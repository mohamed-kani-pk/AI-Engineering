def add(a, b):
    return a + b
  
def subtract(a, b):
    return a - b  
  
def multiply(a, b):
    return a * b
  
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b  

def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot perform modulus by zero.")
    return a % b

def add_numbers(a, b, *c):
    total = a + b
    for num in c:
        total += num
    return total

def power(a, b):
    return a ** b
  
print("Module imported successfully. You can now use the arithmetic functions defined in this module.")