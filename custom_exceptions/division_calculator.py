def division():
    try:
        num1 = float(input("Enter numerator : "))
        num2 = float(input("Enter denominator : "))
        return num1/num2
    except ZeroDivisionError:
        print("Value must not equal to zero")
        return 0

print(division())