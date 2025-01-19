def input_list():
    user_input = input("Enter list elements seperated by space : ")
    lst = user_input.split()
    return lst

L = input_list()

print(f"List : {L}" , "\n ")
num = input("Enter element you want to remove from list : ")

while num in L:
    L.remove(num)
print(L)


lst = [x for x in L if x!=num]
print(lst)