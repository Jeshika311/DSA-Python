dic = {}
num_pairs = int(input("Enter number of key-value pairs : "))

for i in range(num_pairs):
    key = input(f"Enter key {i+1} : ")
    value = int(input(f"Enter value {i+1} : "))
    dic[key] = value
print(dic)

#sort key-value pairs
sorted_dict = sorted(dic.items())
print("Sorted dictionary by key-value pair : \n" , sorted_dict)

#sory by values
sorted_dict = sorted(dic.values())
print("Sorted dictionary by values : \n" , sorted_dict)

#sort by key
sorted_dict = sorted(dic.keys())
print("Sorted dictionary by keys : \n" , sorted_dict)