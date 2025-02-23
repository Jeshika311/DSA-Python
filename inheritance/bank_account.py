#Demonstrate how inheritance can help manage different account types while maintaining common functionality in the parent class.

class BankAccount:
    def __init__(self,balance,number,holder):
        if balance<0:
            raise ValueError("Initial balance can not be negative")
        self.number = number
        self.holder = holder
        self.balance = float(balance) 

    def check_balance(self):
        print(f"Your initial balance is {self.balance}")

    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print("Deposit successfully..!!")
            print(f"New balance : {self.balance}")
        else:
            print("Invalid amount..!!")
            print("Enter valid amount.")

    def withdraw(self,amount):
        if (amount>0 and amount<self.balance):
            self.balance-=amount
            print("Withdraw successfully..!!")
            print(f"New balance : {self.balance}")
        else:
            print("Invalid amount..!!")
            print("Enter valid amount.")
            print("Amount must be less than initial balance and greater than zero.")

    def info(self):
        print("\nAccount Details")
        print(f"Account Number : {self.number}")
        print(f"Account Holder : {self.holder}")
        print(f"Initial Balance : {self.balance}")

    
class SavingsAccount(BankAccount):
    def __init__(self,balance,number,holder,time):
        super().__init__(balance,number,holder)
        self.time = time

    def SI(self):
        simple_interest = (self.balance*2*self.time)/100
        print(f"Simple interest for {self.time} years : {simple_interest}") 

number = int(input("Enter Account number : "))
holder = input("Enter Account Holder name : ")
balance = float(input("Enter your initial balance : "))

bank = BankAccount(balance,number,holder)

time = float(input("Enter time to calculate SI : "))
Interest = SavingsAccount(balance,number,holder,time)

while True:

    print("\nChoose an option : ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check interest")
    print("4. Check balance")
    print("5. Account info")
    print("6. Exit\n")
    option = int(input("Enter any option (1-5): "))

    if option==1:
        amount = float(input("Enter amount to deposit : "))
        bank.deposit(amount)
        Interest.balance = bank.balance     # Update balance in SavingsAccount
    
    elif option==2:
        amount = float(input("Enter amount to withdraw : "))
        bank.withdraw(amount)
        Interest.balance = bank.balance     # Update balance in SavingsAccount

    elif option==3:
        Interest.SI()

    elif option==4:
        bank.check_balance()

    elif option==5:
        bank.info()

    elif option==6:
        print("Exiting.....")
        break

    else:
        print("Enter valid option...")