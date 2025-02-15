def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
num = int(input("Enter number whose factorial you want to find : "))

a = factorial(num)
print(f"Factorial : {factorial(num)}")