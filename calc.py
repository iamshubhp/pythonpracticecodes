# Basic Python Calculator

operator = input("Choose an Operator (+, -, *, /, %): ")

value1 = float(input("Enter your first value: "))
value2 = float(input("Enter your second value: "))

if operator == "+":
    print(f"Addition of {value1} and {value2} is {round(value1 + value2, 2)}")
elif operator == "-":
    print(f"Subtraction of {value1} and {value2} is {round(value1 - value2, 2)}")
elif operator == "*":
    print(f"Multiplication of {value1} and {value2} is {round(value1 * value2, 2)}")
elif operator == "/":
    if value2 != 0:
        print(f"Division of {value1} and {value2} is {round(value1 / value2, 2)}")
    else:
        print("Error: Division by zero is not allowed.")
elif operator == "%":
    if value2 != 0:
        print(f"Remainder of {value1} and {value2} is {round(value1 % value2, 2)}")
    else:
        print("Division by zero is not allowed!")
else:
    print("Invalid operator. Please choose one of +, -, *, /, %.")
