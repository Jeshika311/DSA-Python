fac = int(input("Enter number whose factorial you want to find : "))
factorial = 1
for i in range(1,fac+1):
    factorial*=i
    
print(f"factorial of {fac} is {factorial}")