def input_list():
    user_input = input("Enter list items seperated by spaces : ")
    lst = user_input.split()
    return lst

L = input_list()

max_num = L[0]
min_num = L[0]

for num in L:
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num

print("Maximum number : " , max_num)
print("Minimum number : " , min_num)