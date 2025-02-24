#Use method overriding to calculate the area of different shapes.

class shape:
    def area(self):
        return 0
    
class rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length*self.width
    
class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius

print("Calculate area : ")
print("Enter 1 for rectangle")
print("Enter 2 for circle")
print("Enter 3 for exit")

while True:
    option = int(input("Enter any option : "))

    if option==1:
        length = float(input("Enter length : "))
        width = float(input("Enter width : "))

        rec = rectangle(length,width)
        print(f"Area of Rectangle: {rec.area()}")
    
    elif option==2:
        radius = float(input("Enter radius : "))
        cir = circle(radius)
        print(f"Area of Circle: {cir.area()}")

    elif option==3:
        print("Exiting....")
        break

    else:
        print("Invalid option! Please try again.")