amount = float(input("Enter your initial balance : "))

while True:
    print("Options :-\n1.Check Balance\n2.Withdraw\n3.Deposit\n4.Exit")

    option = int(input("Enter option : "))

    if(option==1):
        print(f"\nYour initial balance is {amount}\n")
    elif(option==2):
        withdraw = float(input("Enter amount you want to withdraw : "))
        if(withdraw<=amount):
            amount-=withdraw
            print(f"\nYour final balance is {amount}\n")
        elif(withdraw>amount):
            print("Balance is less than withdraw amount\nTransaction Fail")
    elif(option==3):
        deposit = float(input("Enter amount you want to deposit: "))
        amount+=deposit
        print(f"\nYour final balance is {amount}\n")
    elif(option==4):
        print("\n__Exiting__\n")
        break
    else:
        print("Enter a valid option")