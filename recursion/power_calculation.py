def power(x,y):
    if y==0:
        return 1
    elif y<0:
        return 1/power(x , -y)
    else:
        return x*power(x, y-1)
    
x = float(input("Enter the base : "))
y = float(input("Enter the exponent : "))
print(f"{x} raised to the power y is : {power(x,y)}") 