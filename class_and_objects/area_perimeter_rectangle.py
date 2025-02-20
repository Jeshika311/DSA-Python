class rectangle:
    def __init__(self , l , w):
        self.length = l
        self.width = w

    def area(self):            #class method for finding area of rectangle
        return self.length*self.width
    
    def perimeter(self):       #class method for finding perimeter of rectangle
        return 2*(self.length+self.width)
    
length = float(input("Enter length of rectangle : "))
width = float(input("Enter width of rectangle : "))
    
obj1 = rectangle(length,width)

print("Area of rectangle is : " , obj1.area())
print("Perimeter of rectangle is : " , obj1.perimeter())  