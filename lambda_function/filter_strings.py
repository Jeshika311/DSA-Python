string = str(input("Enter a string : "))

#get strings that are started with a

filtered_string = " ".join(filter(lambda x : x[0].lower() == 'a' , string.split()))
print(filtered_string) 