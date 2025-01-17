def input_list():
    user_list = input("Enter list elements seperated by spaces : ")
    lst = list(map(int, user_list.split()))
    return lst

L = input_list()
print("User list : " , L)

if len(L)>2:
    L.sort()
    print("Second largest element in list : " , L[-2])
else:
    print("List should have more than two elements")