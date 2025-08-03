def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    if number2 == 0:
        raise ValueError("Cannot divide by zero.")
    return number1 / number2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculate():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    operation = input("Enter the operation (+, -, *, /): ")
    if operation not in operations:
        raise ValueError(f"Operation '{operation}' is not supported.")
    result = operations[operation](first_number, second_number)
    print(f"The result of {first_number} {operation} {second_number} is: {result}")


calculate()