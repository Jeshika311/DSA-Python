n = int(input("Enter the number of rows you want : "))

for i in range(n-1):
    for j in range(i+1):
        print(" ", end = "")
    for k in range(n-i):
        print("*" , end = " ")
    print()

for i in range(n):
    for j in range(n-i):
        print(" " , end = "")
    for k in range(i+1):
        print("*", end = " ")
    print()