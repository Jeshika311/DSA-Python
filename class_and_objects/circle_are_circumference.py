class circle:
    def __init__(self,radius):
        self.__radius = float(radius)

    #getter for radius

    def get_radius(self):
        return self.__radius
    
    #setter for radius

    def set_radius(self,radius):
        if radius<0:
            print("Radius should be positive")
        elif radius==0:
            print("Radius can't be zero")
            print("Radius should be non zero positive number")
        else:
            self.__radius = radius
            print(f"Rradius : {self.__radius}")
    
    #class method for calculating area of circle

    def area(self):
        return 3.14*self.__radius*self.__radius
    
    #class method for calculating area of circle

    def circumference(self):
        return 2*3.14*self.__radius
    
radius = float(input("Enter radius of circle : "))
circle1 = circle(radius)
Area = print(f"Area of circle is : {circle1.area()}")
circumference = print(f"Circumference of circle is : {circle1.circumference()}")