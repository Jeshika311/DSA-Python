x = input("Enter any character : ")

if(x.isalpha()):
    print("Given character is alphabet")
elif(x.isalnum()):
    print("Given character is number")   
else:
    print("It is a special character")