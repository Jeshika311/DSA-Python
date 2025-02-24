class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

class student(person):
    def __init__(self,name,age,grade):
        person.__init__(self,name,age)
        self.grade = grade

    def info(self):
        person.info(self)
        print(f"Grade : {self.grade}")

name = input("Enter student name : ")
age = int(input("Enter student age : "))
grade = input("Enter student grade : ")

student1 = student(name , age , grade)
student1.info()