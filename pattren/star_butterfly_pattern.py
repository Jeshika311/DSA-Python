n = int(input("Enter the number of rows you want : "))

for i in range(n-1):
    for j in range(i+1):
        print("*" , end = " ")
    for k in range(2*(n-i)-2):
        print(" " , end = " ")
    for j in range(i+1):
        print("*" , end = " ")
    print()

for i in range(n):
    for j in range(n-i):
        print("*" , end = " ")
    for k in range(2*i):
        print(" " , end = " ")
    for j in range(n-i):
        print("*" , end = " ")
    print()