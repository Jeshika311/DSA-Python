def input_set():
    set_input = input("Enter set elements seperated by space : ")
    s = set(set_input.split())
    return s

S1 = input_set()
print(f"Set 1 : {S1}")
S2 = input_set()
print(f"Set 2 : {S2}")

if S1.issubset(S2):
    print("\nSet 1 is subset of Set 2\nOR\nSet 2 is superset of set 1")
elif S2.issubset(S1):
    print("\nSet 2 is subset of set 1\nOR\nSet 1 is superset of set 2")
else:
    print("\nNo set is subset of another one")