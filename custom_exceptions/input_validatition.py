def user_input():
        input_user = int(input("Enter any positive number : "))
        if(input_user<=0):
                raise ValueError("Value should be a positive integer")
        return 1
    
print(user_input())