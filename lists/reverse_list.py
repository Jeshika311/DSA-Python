def input_list():
    user_input = input("Enter list items seperated by spaces : ")
    lst = user_input.split()
    return lst

L = input_list()
print("User list : " , L)

reversed_list = []
for item in L:
    reversed_list.insert(0, item)
print("Reversed list : ", reversed_list)