def input_set():
    set_input = input("Enter set elements seperated by space : ")
    s = set(set_input.split())
    return s 

S1 = input_set()
print(f"Set1 : {S1}")
S2 = input_set()
print(f"Set 2 : {S2}")

if S1.issuperset(S2):
    S3 = S1.difference(S2)
    print(f"Compliment of Set 2 is : {S3}")
elif S2.issuperset(S1):
    S3 = S2.difference(S1)
    print(f"Compliment of set 1 is : {S3}")
else:
    print("One set should of subset of another one")