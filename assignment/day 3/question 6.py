
def add(a, b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
def calculate(operand1, operand2, func):
    return func(operand1, operand2)
print("Testing with 10 and 5:")
print("Addition:", calculate(10, 5, add))        
print("Subtraction:", calculate(10, 5, subtract)) # 5
print("Multiplication:", calculate(10, 5, multiply)) # 50
print("Division:", calculate(10, 5, divide))     # 2.0

print("\nTesting with 7 and 3:")
print("Addition:", calculate(7, 3, add))         # 10
print("Subtraction:", calculate(7, 3, subtract)) # 4
print("Multiplication:", calculate(7, 3, multiply)) # 21
print("Division:", calculate(7, 3, divide))      # 2.333...

print("\nTesting division by zero:")
print("Division:", calculate(7, 0, divide))      # Error message
