def input_list():
    user_input = input("Enter list items seperated by spaces : ")
    lst = user_input.split()
    return lst

L = input_list()
print("User list : " , L)

half = len(L)//2
first_half = L[:half]
second_half = L[half:]

print(f"First half : {first_half}")
print(f"Second half : {second_half}")