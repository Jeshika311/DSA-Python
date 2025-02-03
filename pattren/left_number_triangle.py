n = int(input("Enter the number of rows you want : "))

for i in range(n):
    p=1
    for j in range(n-i):
        print(" " , end = " ")

    for j in range(i+1):
        print(p , end = " ")
        p+=1
    print()