def rotate_list(input_list , k):
    k = k% len(input_list)
    return input_list[-k:] + input_list[:-k]

def input_list():
    user_input = input("Enter list items seperated by space : ")
    lst = user_input.split()
    return lst

L = input_list()
print("User list : " , L)

k = int(input("Enter index from which you want to rotate your list to the right : "))

a = rotate_list(L,k)
print("Rotated list : " , a)