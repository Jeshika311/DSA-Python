class car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = float(price)

    def compare(self , other_car):
        if(self.price > other_car.price):
            print(f"{self.brand} is more expansive than {other_car.brand}")
        elif(self.price < other_car.price):
            print(f"{other_car.brand} is more expansive than {self.brand}")
        else:
            print(f"{self.brand} and {other_car.brand} have the same price")

def get_car_details(car_number):
    brand = input(f"Enter brand of {car_number} : ")
    model = input(f"Enter model of {car_number} : ")
    price = input(f"Enter price of {car_number} : ")
    return car(brand,model,price)

car1 = get_car_details(1)
car2 = get_car_details(2)
car1.compare(car2)