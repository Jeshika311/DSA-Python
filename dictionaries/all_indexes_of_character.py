char = str(input("Enter a string : "))
dic = {}

for index , charac in enumerate(char):
    if charac not in dic:
        dic[charac] = []
    dic[charac].append(index)

for char , index in dic.items():
    print(f"{char} : {index}")