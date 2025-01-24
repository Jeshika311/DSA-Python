def input_list():
    user_input = input("Enter list items seperated by spaces : ")
    lst = user_input.split()
    return lst

L = input_list()
print("User list : " , L)

subsets =[[]]

for elem in L:
    subsets += [subset + [elem] for subset in subsets]
print(subsets)