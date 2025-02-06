n = int(input("Enter the number of rows you want : "))

for i in range(n):
    for j in range(n-i):
        print(" " , end = " ")
    for k in range(i):
        print("*" , end = " ")
    print()

for i in range(n):
    for j in range(i):
        print(" " , end =" ")
    for k in range(n-i):
        print("*" , end = " ")
    print()
