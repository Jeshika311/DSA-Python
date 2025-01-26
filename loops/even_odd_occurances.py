my_list = input("Enter a list seperated by space : ")
my_list = [int(num) for num in my_list.split()]
odd = 0
even = 0
for num in my_list:
    if(num%2==0):
        even+=1
    else:
        odd+=1
print(f"(Total number of occurances of odd numbers is {odd})")
print(f"(Total number of occurances of even numbers is {even})")
