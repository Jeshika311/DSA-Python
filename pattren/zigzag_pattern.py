n = int(input("Enter the number of rows you want : "))

for i in range(n):
    for j in range(n-i):
        print(" " , end = "")
    for k in range(i+1):
        if(k==i or k==0):
            print("*" , end = " ")
        else:
            print(" " , end = " ")

    for j in range(2*(n-i)-2):
        print(" " , end ="")
    for k in range(i+1):
        if(k==i or k==0):
            print("*" , end = " ")
        else:
            print(" " , end = " ")
    print()