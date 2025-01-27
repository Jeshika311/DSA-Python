num = int(input("Enter any number whose multiple you want to find : "))
print("Enter 2 numbers between which you want to find divisible of any number : ")
num1= int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

for i in range(num1, num2):
    if i%num==0:
        print(i)