def fibonacci(n):
    if n<=0:
        return "Input should be a positive integer"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter number upto which you want to find fibonacci sequence : "))
print("")
print("Fibonacci sequence : ")
for i in range(1,n+1):
    print(fibonacci(i))