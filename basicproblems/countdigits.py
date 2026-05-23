a = int(input("Enter the number : "))
count = 0
while a>0:
    a = a // 10
    #print("a :",a)
    count += 1
    #print("count :",count)

print(count, " digits") 