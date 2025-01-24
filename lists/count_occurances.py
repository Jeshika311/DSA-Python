def input_list():
    user_input = input("Enter list elements seperated by spaces : ")
    lst = user_input.split()
    return lst

L = input_list()
print("user list : " , L)
n = int(input("Enter number whose occurances you want to count in your list : "))
print(L.count(f"{n}"))