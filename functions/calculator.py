def addition():
    return a+b
def subtraction():
    return a-b
def multiply():
    return a*b
def divide():
    if b==0:
        print("zero is not dividable")
    else:
        return a/b
def modulos():
    return a%b
def power():
    return a ** b

def floor_division():
    if b == 0:
        return "Cannot divide by zero"
    return a // b
while True:
    a = int(input("a :"))
    b= int(input("b :"))
    operation = input("Enter the operator( + , - , * , / , % , ** , //) : ")
    if operation == "+":
        print("Addition :",addition())
    elif operation == "-":
        print("Subtraction :",subtraction())
    elif operation == "*":
        print("Multiply :",multiply())
    elif operation == "/":
        print("divide : ",divide())
    elif operation == "%":
        print("Modulos :",modulos())
    elif operation == "**":
        print("Power :",power())
    elif operation == "//":
        print("Floor Division :",floor_division())
    else:
        print("undefined operator")

    choice = input("Do you want to continue? yes/no :")
    if choice.lower == "no":
        print("calculator closed")
        break
