def input_set():
    set_input = input("Enter set elements seperated by space : ")
    s = set(set_input.split())
    return s 
    
S1 = input_set()
print(f"Set 1 : {S1}")
S2 = input_set()
print(f"Set 2 : {S2}")
S3 = input_set()
print(f"Set 3 : {S3}")

S4 = S1.union(S2,S3)

print(f"Union of all 3 sets is : {S4}")