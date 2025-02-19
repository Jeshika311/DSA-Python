def input_list():
    list_input = input("Enter elements of list seperated by spaces : ")
    lst = list(map(int , list_input.split()))
    return lst

a = input_list()

print(f"List : {a}")

from functools import reduce

product = reduce(lambda x,y : x*y , a)
print(product)