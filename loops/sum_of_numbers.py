num = int(input("Enter number upto which you want to find sum of numbers : "))
sum = 0 

for i in range(num+1):
    sum+=i
print(f"Sum of fisrt {num} numbers is {sum}")