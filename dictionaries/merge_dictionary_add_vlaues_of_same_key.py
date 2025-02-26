def dictionary(n):
    dic = {}
    num = int(input(f"Enter number of key-value pairs of {n} dictionary : "))

    for i in range(num):
        key = input(f"Enter key {i+1} : ")
        value = int(input(f"Enter value {i+1} : "))
        dic[key] = value
    return dic
    
dic1 = dictionary(1)
print("Dictionary 1 : ", dic1)
dic2 = dictionary(2)
print("Dictionary 2 : " , dic2)

for i in dic2:
    if i in dic1:
        dic1[i]+=dic2[i]
    else:
        dic1[i] = dic2[i]

print(f"Sorted dictionary : {dic1}")