percentage = float(input("Enter your percentage : "))

if(percentage>=90 and percentage<=100):
    print("Grade = A")
elif(percentage>=75 and percentage<90):
    print("Grade = B")
elif(percentage>=50 and percentage<75):
    print("Grade = C")
elif(percentage>=0 and percentage<50):
    print("Fail")
else:
    print("Enter a valid percentage\nPercentage should be between 0 to 100")
print("___THANKYOU___")