class account:
    def __init__(self,number,holder,balance):
        self.account_number = number
        self.account_holder = holder
        self.balance = float(balance)

    def deposit(self):
        deposit_money = float(input("Enter money you want to deposit : "))
        if deposit_money>0:
            self.balance+=deposit_money
            print(f"\nSuccessfully deposit..!!\nNew balance : {self.balance}")
        else:
            print("Enter valid amount")
    
    def withdraw(self):
        withdraw_money = float(input("Enter amount you want to withdraw : "))
        if(withdraw_money<=self.balance and withdraw_money>0):
            self.balance-=withdraw_money
            print(f"\nSuccessfully Withdraw..!!\nNew balance {self.balance}")
        else:
            print("Withdraw money should less than initial balance")

    def info(self):
        print(f"Account holder : {self.account_holder}")
        print(f"Account number : {self.account_number}")
        print(f"Initial balance : {self.balance}")

number = int(input("Enter your account number : "))
name = str(input("Enter account holder name : "))
balance = float(input("Enter your initial balance : "))

holder1 = account(number , name , balance)

#taking option from the user

print("\nChoose an option : ")
print("1. Deposit")
print("2. Withdraw")
print("3. Account info")
print("4. Exit\n")

option = int(input("Enter any option : "))

if(option==1):
    holder1.deposit()
elif(option==2):
    holder1.withdraw()
elif(option==3):
    holder1.info()
elif(option==4):
    print("Exiting...")
else:
    print("Enter a valid option")