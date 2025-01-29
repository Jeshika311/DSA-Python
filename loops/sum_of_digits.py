number = int(input("Enter any number whose sum you want to find : "))

sum = 0
while(number>0):
    digit = number%10
    sum+=digit
    number = number//10

print(f"The sum of digits is {sum}")