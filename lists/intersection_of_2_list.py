def input_list():
    user_input = input("Enter list items seperated by spaces : ")
    lst = user_input.split()
    return lst

L1 = input_list()
print("First list : " , L1)
L2 = input_list()
print("Second list : " , L2)
lst = [x for x in L1 if x in L2]
print(f"Intersection elements : {lst}")