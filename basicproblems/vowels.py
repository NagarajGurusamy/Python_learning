a= input("Enter the text: ")
vowels= "aeiouAEIOU"
count = 0
for i in a:
    if i in vowels:
        count += 1
print("Vowels", count)