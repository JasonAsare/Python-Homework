"""
Nested if calculator
"""

num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Squared (**)")
print("6. Modulus (%)")

operation = input("+, -, *, /, **, %: ")

if operation == "+":
    print('The answer is', num1 + num2)
else:
    if operation == "-":
        print("The number is", num1 - num2)
    else:
        if operation == "*":
            print("The number is", num1 * num2)
        else:
            if operation == "/":
                print("The number is", num1 / num2)
            else:
                if operation == "**":
                    print("The number is", num1 ** num2)
                else:
                    if operation == "%":
                        print("The number is", num1 % num2)
                    else:
                        print("Invalid key")
                        