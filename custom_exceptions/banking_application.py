class InsufficientFundsError(Exception):
    """raise when withdraw amount is more than their initial balance"""
    pass
try:
    balance = float(input("Enter initial balance : "))
    amount = float(input("Enter amount you want to withdraw : "))
    if(amount>balance):
        raise InsufficientFundsError
    else:
        balance2 = balance - amount
        print(f"Balance after withdrawing {amount} from {balance} is {balance2}")
except InsufficientFundsError:
    print("InsufficientFundsError : Initial balance must greater than withdraw amount")