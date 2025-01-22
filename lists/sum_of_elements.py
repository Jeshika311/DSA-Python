def input_list():
    user_input = input("Enter elements seperated by spaces : ")
    lst = user_input.split()
    return lst
L = input_list()
print("User list : " , L)

sum = 0
for i in L:
    sum+=int(i)
print("Sum of all elements of list is : " , sum)