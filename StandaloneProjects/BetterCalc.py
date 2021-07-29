
num1 = (input("Enter a Number: "))
operator = input("Enter a Operator: ")
num2 = (input("Enter another Number: "))

if num1.__contains__("."):
    num1 = float(num1)
    num2 = float(num2)
elif num2.__contains__("."):
    num1 = float(num1)
    num2 = float(num2)
else:
    num1 = int(num1)
    num2 = int(num2)

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("*'" + operator + "'" + " Not a Valid Operator*")