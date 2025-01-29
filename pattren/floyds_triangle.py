n = int(input("Enter the number of rows you want : "))
p=1

for i in range(n):
    for j in range(i+1):
        print(p , end = " ")
        p+=1
    print()