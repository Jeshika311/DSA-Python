principle = float(input("Enter principle : "))
rate = float(input("Enter rate : "))
time = float(input("Enter time : "))

def SI(p,r,t):
    SimpleInterest = (p*r*t)/100
    return SimpleInterest

SI(principle,rate,time)
simple_interest = SI(principle,rate,time)

print(f"Simple Interest of given values is {simple_interest}")