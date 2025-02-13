n = int(input("Enter value of n : "))
r = int(input("Enter value of r : "))

def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac*=i
    return fac

factorial(n)
factorial(r)
factorial(n-r)

formula = factorial(n)/(factorial(n-r)*factorial(r))

print(f"Answer for given value of n = {n} and r = {r} is {formula}")