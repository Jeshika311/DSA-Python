class car:
    def __init__(self, make, model, year, color, fuel_type, price):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type
        self.price = price

    def info(self):
        return("\nCar details : "
        f"\nManufacturer of car : {self.make}"
        f"\nModel of car : {model}"
        f"\nManufacturing Year of car : {self.year}"
        f"\nColor of car : {self.color}"
        f"\nType of fuel of car : {self.fuel_type}"
        f"\nPrice of car : {self.price}")

make = str(input("Enter the manufacturer of the car : "))
model = str(input("Enter the model of the car : "))
year= int(input("Enter the manufacturing year of the car : "))
color = str(input("Enter the color of the car : "))
fuel_type =str(input("Enter the type of fuel the car uses : "))
price = float(input("Enter the price of car : "))

a = car(make, model, year, color, fuel_type, price)
print(a.info())