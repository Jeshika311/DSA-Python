def input_list():
    list_input = input("Enter elements of list seperated by spaces : ")
    lst = list(map(int , list_input.split()))
    return lst

a = input_list()

print(f"List : {a}")

a = list(filter(lambda x : x%2==0 , a))
print(f"Even numbers in list : {a}")