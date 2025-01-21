def input_list():
    user_input = input("Enter list items seperated by spaces : ")
    lst = user_input.split()
    return lst

L1 = input_list()
print("List 1 : " , L1 , "\n")

L2 = input_list()
print("List 2 : " , L2 , "\n")

L1.extend(L2)
print(f"Merged list : {L1}")

L1.sort()
print(f"Sorted list in ascending order : {L1}")