n = int(input("Enter the number of rows you want : "))

for i in range(n):
    for j in range(n-i):
        print(" " , end = " ")

    for k in range(2*i+1):
        print("*" , end = " ")

    print()