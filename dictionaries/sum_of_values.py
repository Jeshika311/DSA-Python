dictionary = {}
num_pairs = int(input("Enter number of key-value pairs : "))

for i in range(num_pairs):
    key = input(f"Enter key {i+1} : ")
    value = int(input(f"Enter value {i+1} : "))
    dictionary[key] = value 
print(dictionary)

sum = 0
for i in dictionary.values():
    sum+=i
print(f"sum of values is : {sum}")