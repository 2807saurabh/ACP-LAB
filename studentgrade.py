students = ["Rohan:a"]

def add():
    n=int(input("Enter number of student to add:"))

    for i in range (n):
        name=input("enter name:")
        grade=input("Enter grade:")
    students.append([name,grade])




print(students)