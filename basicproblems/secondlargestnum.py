a = input("enter the number : ").split()
a=[int(x) for x in a]
print(a)
a= list(set(a))
a.sort()
print(a)
print("second largest number : ",a[-2])