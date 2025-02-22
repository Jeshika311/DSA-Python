class product:
    total_products = 0             #class variable to count total products
    def __init__(self,name,price,discount):

        if price <= 0:             # Ensuring price is positive
            raise ValueError("Error: Price must be a positive number.")
        if discount < 0 or discount >= price:            # Ensuring valid discount
            raise ValueError("Error: Discount must be non-negative and less than the price.")
        
        self.name = name
        self.price = float(price)
        self._discount = float(discount)
        product.total_products+=1          #increment total products count

    #getter for discount

    def get_discount(self):
        return self._discount
    
    #setter for discount

    def set_discount(self , discount):
        if discount < 0:
            print("Error: Discount can't be negative")
        elif discount >= self.price:
            print("Error: Discount must be less than price!")
        else:
            self._discount = discount
            print(f"Discount applied: ${self._discount}")


    #static method for convert USD into INR

    @staticmethod
    def convert(price):
        return round(price*86.93 , 2)
    
    #class method to display total products created

    @classmethod
    def product_summary(cls):
        print(f"Total products created : {cls.total_products}")
    
    #display product details 

    def info(self):
        print(f"\nProduct name : {self.name}")
        print(f"Original price : ${self.price}")
        print(f"Discount :  ${self._discount:.2f}")
        print(f"Price After Discount (USD): ${self.price - self._discount:.2f}")

# Function to create multiple product instances
       
def total_products():
    product_list = []
    product_number = int(input("Enter the number of products : "))

    for i in range(1,product_number+1):
        name = input(f"\nProduct name {i} : ")
        price = float(input(f"Original price {i} : "))
        discount = float(input(f"Enter discount {i} : "))

        obj = product(name,price,discount)
        product_list.append(obj)

    return product_list

# Creating and displaying product details

products = total_products()

for product in products:
    product.info()
    print()

# Display total products
product.product_summary()

if products:
    print("\nConverted original Prices to INR:")
    for product in products:
        inr_price = product.convert(product.price)
        print(f"{product.name}: ₹{inr_price}")