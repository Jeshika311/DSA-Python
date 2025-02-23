#Demonstrate polymorphism by calling the speak() method from different animal objects.

class animal:
    def speak():
        print("Some generic animal sound")

class dog(animal):
    def speak():
        print("Dog : Bark")

class cat(animal):
    def speak():
        print("Cat : Meow")

a = animal.speak()
d = dog.speak()
c = cat.speak()