def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def power(x, y):
    return x ** y

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': power
}

print("Welcome to the Simple Calculator!")
print("Supported operations: + - * / ^ (for power)")

while True:
    try:
        num1 = float(input("\nEnter first number: "))
        op = input("Enter operation: ")
        num2 = float(input("Enter second number: "))

        if op not in operations:
            print("Invalid operation! Try +, -, *, /, or ^.")
            continue

        result = operations[op](num1, num2)
        print(f"Result: {result}")

        again = input("Do another calculation? (y/n): ").lower()
        if again != 'y':
            print("Thanks for using the calculator!")
            break

    except ValueError:
        print("Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")
