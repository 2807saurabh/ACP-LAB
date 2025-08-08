#for loop 
#Program 1)
n = int(input("Enter the number:"))
for i in range(1,n+1):
    print(i)


#Program 2)
n = int(input("Enter the number:"))
for i in range(2,n+2,2):
    print(i)

#Program 3)
n = int(input("Enter the number:"))
for i in range(1,n+2,2):
    print(i)

#Program 4)
n = int(input("Enter the number:"))
for i in range(n):
    print(2**i,end=" ")


#Program 8)
for i in range(3):
    print("A B C")


#Program 9)
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()


#Program 10)
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(n-i):
        print(chr(65+j),end=" ")
    print()


#Program 11)
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(1,i+2):
        print(j,end=" ")
    print()


#Program 12)
n = int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()