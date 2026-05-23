a = int(input("Enter a number : "))
reverse = 0
while a>0:
    digit = a%10 
    #print(digit)
    reverse = reverse *10 + digit
    #print(reverse)
    a = a // 10 
    #print(a)

print("Reverse :", reverse)
