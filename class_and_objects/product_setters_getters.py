class Product:
    def __init__(self,name,price):
        self._name = name
        self._price = float(price)

    #getter for price

    def get_price(self):
        return self._price
        
    #setter for price

    def set_price(self , new_price):
        if self._price<0:
            print("Error : Price can't be negative")
        elif new_price>self._price:
            print("Discounted price should be less than actual price")
        else:
            print(f"Price updated successfully..!! New price : {new_price}")

    def info(self):
        print(f"Product name : {self._name}")
        print(f"Product price : {self._price}")

name = input("Enter product name : ")
price = float(input("Enter price of product : "))
product1 = Product(name,price)
product1.info()

new_price = float(input("Enter price after discount : "))
product1.set_price(new_price)