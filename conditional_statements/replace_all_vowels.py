def replace_vowels(input_str):
    vowels = "aeiouAEIOU"
    output_str = ""
    for char in input_str:
        if char in vowels:
            output_str += '*'
        else:
            output_str += char

    return output_str

string = str(input("Enter a string in which you want to replace all vowels with * : "))

a = replace_vowels(f"{string}")
print(a)