a= int(input("enter number1 : "))
b= int(input("enter number2 : "))
c = input("enter operatr( + , - , * , / ) : ")

if c == "+":
    print("add :",a+b)
elif c == "-":
    print("sub :", a-b)
elif c == "*":
    print("Multiply :",a*b)
elif c == "/" :
    if b==0:
        print("not divisible by 0")
    else:
        print("divide :",a/b)

else :
    print("invalid operator")
        

