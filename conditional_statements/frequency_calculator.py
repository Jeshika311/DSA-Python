string = str(input("Enter a string : "))
frequency = {}

for x in string:
    if x.isalpha():
        if x in frequency:
            frequency[x] += 1
        else:
            frequency[x] = 1

for letter , count in frequency.items():
    print(f"{letter} : {count}")