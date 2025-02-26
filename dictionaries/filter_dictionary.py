dic = {}
num_pairs = int(input("Enter number of key-value pairs : "))

for i in range(num_pairs):
    key = input(f"Enter key {i+1} : ")
    value = input(f"Enter value {i+1} : ")
    dic[key] = value
print(dic)

#filter by value
filtered_dict = {key : value for key , value in dic.items() if value>5}
print("Dictionary whose value is greater than 5 : ", filtered_dict)

#filter by key
# filtered_dict = {key : value for key , value in dic.items() if key in ['a' , 'c']}
# print(filtered_dict)

# #filtered by key-value
# filtered_dict = {key : value for key , value in dic.items() if (key,value) in [('a', 1) , ('c', 3)]}
# print(filtered_dict)