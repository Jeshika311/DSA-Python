string = str(input("Enter a string : "))
frequency = {}

for i in string:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

max_key = max(frequency , key= frequency.get)
max_frequency = frequency[max_key]
print(f"The most commomm character is '{max_key}' with a frequency of {max_frequency}")