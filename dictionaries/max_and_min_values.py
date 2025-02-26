dic = {}
num_pairs = int(input("Enter number of key-value pairs : "))

for i in range(num_pairs):
    key = input(f"Enter key {i+1} : ")
    value = int(input(f"Enter value {i+1} : "))
    dic[key]=value
print(dic)

max = 0
min = 0

for i in dic.values():
    if max<i:
        max = i
print(f"Maximum value = {max}")
    
for i in dic.values():  
    if min>i:
        min = i
print(f"Minimum value = {min}")
    