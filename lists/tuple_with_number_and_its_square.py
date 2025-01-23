def input_list():
    user_input = input("Enter list items seperated by spaces : ")
    lst = list(map(int , user_input.split()))
    return lst

L = input_list()
print("User list : " , L)

output = [(num , num**2) for num in L]

print(f"Original list : {L}")
print(f"Tuple : {output}")