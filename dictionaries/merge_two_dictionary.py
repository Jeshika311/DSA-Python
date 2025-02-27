def dictionary(n):
    dic = {}
    num_pairs = int(input(f"Enter number of key-value pairs in {n} dictionary : "))

    for i in range(num_pairs):
        key = input(f"Enter key {i+1} : ")
        value = input(f"Enter value {i+1} : ")
        dic[key] = value
    return dic

dic1 = dictionary(1)
print(dic1)
dic2 = dictionary(2)
print(dic2)

dic1.update(dic2)
print("Final Dictionary after merge both dictionaries : \n" , dic1)