n = int(input("Enter the number of rows you want : "))
p=64

for i in range(n):
    for j in range(n-i):
        print(" " , end =" ")
    for k in range(2*i-1):
        print(chr(p) , end = " ")
    p+=1
    print()

for i in range(n):
    for j in range(i):
        print(" " , end = " ")
    for k in range(2*(n-i)-1):
        print(chr(p) , end = " ")
    p-=1
    print()