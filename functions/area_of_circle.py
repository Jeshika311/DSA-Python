radius = float(input("Enter radius of circle : "))

def AreaCircle(radius):
    area = 3.14*radius*radius
    return area

AreaCircle(radius)
area = AreaCircle(radius)
print(f"Area of circle for given radius is {area}")