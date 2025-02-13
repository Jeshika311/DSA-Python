principle = float(input("Enter principle : "))
time = float(input("Enter time : "))
rate = float(input("Enter rate : "))
n = float(input("Enter number of times interest applied per time period : "))

def CI(p,t,r,n):
    A = p * (1 + r/n)**(n*t) 
    CompoundInterest = A - p
    return CompoundInterest
    
CI(principle,time,rate,n)
compound_interest = CI(principle,time,rate,n)

print(f"Compound interest for given values is {compound_interest}")