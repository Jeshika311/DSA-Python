n = int(input("Enter the number of rows you want : "))

for i in range(n):
    for j in range(n-i):
        print(" ", end = "")
    for k in range(i+1):
        if(k==0 or k==i or k==n-1):
            print("1" , end = " ")
        else:
            print(i , end = " ")
    print()