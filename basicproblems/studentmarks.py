students = {}
n=int(input("enter the students range in class : "))
for i in range(n):
    name = input("Enter student name : ")
    mark = int(input("enter the student mark : "))

    students[name] = mark

print(students)