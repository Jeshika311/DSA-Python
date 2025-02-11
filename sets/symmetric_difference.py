#symmetric difference with the help of union, itersection and difference operation

def input_set():
    set_input = input("Enter set elements seperated by spaces : ")
    s = set(set_input.split())
    return s

S1 = input_set()
print(f"set 1 : {S1}")
S2 = input_set()
print(f"Set 2 : {S2}")

S3 = S1.union(S2)
S4 = S1.intersection(S2)

S5 = S3.difference(S4)
print(f"Symmetric difference between two sets is : {S5}")