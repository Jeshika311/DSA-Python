str1 = str(input("Enter first string : ")).lower()
str2 = str(input("Enter second string : ")).lower()

sorted_str1 = sorted(str1.replace(" " , ""))
sorted_str2 = sorted(str2.replace(" " , ""))

if sorted_str1 == sorted_str2:
    print(f"'{str1}' and '{str2}' are anagrams")
else:
    print(f"'{str1}' and '{str2}' are not anagrams")