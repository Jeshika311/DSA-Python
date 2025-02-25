char = str(input("Enter any character : "))

dic ={}
for i in char:
    if i not in dic:
        dic[i] = char.find(i)
        
for i,s in dic.items():
    print(f"{i} : [{s}]")