list_of_tuples = [(1, 2), (3, 4), (5, 6)]
sum = 0

for tup in list_of_tuples:
    for num in tup:
        sum+=num

print(f"list of tuples : {list_of_tuples}")
print("")
print(f"Sum of elements is : {sum}")