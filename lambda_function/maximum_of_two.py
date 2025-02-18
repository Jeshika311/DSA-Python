maximum = lambda num1 , num2 : num1 if num1>num2 else num2
num1 = int(input("Enter 1st number : ")) 
num2 = int(input("Enter 2nd number : "))
print("Greater number is : " , maximum(num1,num2))