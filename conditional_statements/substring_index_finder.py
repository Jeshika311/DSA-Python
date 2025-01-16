string = str(input("Enter any string : "))
substring = str(input("Enter substring you want to find : "))

print(string.find(f"{substring}") , "is the index of the given substring")
print("Index -1 represents that the substring is not present in the given string")