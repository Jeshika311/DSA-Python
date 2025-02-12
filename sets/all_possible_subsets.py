def input_set():
    set_input = input("Enter elements of set seperated by space : ")
    s = set(set_input.split())
    return s

s = input_set()
s2 = list(s)
subsets = [[]]
for i in s2:
    subsets += [subset + [i] for subset in subsets]
print("Possible subsets : " , subsets)