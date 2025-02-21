class person:
    def __init__(self,n,a,c):
        self.name = n
        self.age = a
        self.city = c

    def info(self):
        print(f"My name is {self.name}. I am {self.age} years old. I am from {self.city}")

name = str(input("Enter you name : "))
age = int(input("Enter your age : "))
city = str(input("Enter your city : "))

a = person(name , age , city)
a.info()