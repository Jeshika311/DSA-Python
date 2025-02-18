def input_list():
    list_input = input("Enter elements of list seperated by spaces : ")
    lst = list(map(int , list_input.split()))
    return lst

a = input_list()

print(f"List : {a}")

squares = list(map(lambda x : x**2 , filter(lambda x : x%2!=0 , a)))
print("squares of odd numbers is : " , squares)