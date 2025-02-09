print("Basic Calculations :\n1.Addition\n2.Subtraction\n3.Division\n4.Multiply\n ")

option = int(input("Enter option : "))
   
if(option==1 or option==2 or option==3 or option==4):

    num1 = float(input("Enter 1st number : "))
    num2 = float(input("Enter 2nd number : "))

    if(option==1):  
       print("Addition = ", num1+num2)

    elif(option==2):    
        print("Subtraction = ", num1-num2)

    elif(option==3):
        print("Division = ", num1/num2)

    elif(option==4):
        print("Multiplication = ", num1*num2)

else:
    print("Enter a valid option")

print("___Thank you___")