def input_list():
    user_input = input("Enter list items seperated by spaces : ")
    lst = user_input.split()
    return lst

L = input_list()
print("User list : " , L)
lst = [x for x in L if L.count(x) > 1]
print(lst)