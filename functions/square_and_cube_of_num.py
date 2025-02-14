a = int(input("Enter any number whose square and cube you want to find : "))

def square(a):
    squaree = a*a
    return squaree

def cube(a):
    cubee = a*a*a
    return cubee

square(a)
squaree = square(a)
cube(a)
cubee = cube(a)

print(f"Square of given number is {squaree}")
print(f"Cube of given number is {cubee}")