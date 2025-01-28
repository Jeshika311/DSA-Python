print("Enter any password consisting of :-\nAtleast 8 characters\nContain both uppercase and Lowercase characters\nContain atleast one digit")
password = input("Enter password : ")
has_uppercase = False
has_lowercase = False
has_digit = False

for char in password:
    if 'A' <= char <= 'Z':
        has_uppercase = True

    elif 'a' <= char <= 'z':
        has_lowercase = True

    elif '0' <= char <= '9':
        has_digit = True

if(password[7:] and password.isalnum()):
    if(has_uppercase==True and has_lowercase==True and has_digit==True):    
        print(f"{password} is a valid password")
    else:
        print(f"{password} is not a valid password")

else:
    print("Password should have atleast 8 characters")