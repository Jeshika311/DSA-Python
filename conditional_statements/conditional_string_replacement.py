string = str(input("Enter any string : "))

if(len(string)>20):
    str1 = str(input("Enter word that you want to replace : "))
    str2 = str(input("Enter new word from which you want to replace your old word : "))

    print(string.replace(f"{str1}" , f"{str2}"))

else:
    print("Length of string must greater than 20")