def input_list():
    list_input = input("Enter temperatues in Celsius seperated by spaces : ")
    lst = list(map(int ,list_input.split()))
    return lst

a = input_list()
print("Temperature in Celsius : " , a)

Fahrenheit = list(map(lambda x : (x*9/5) +  32 , a))
print(f"Temperature in fahrenheit : {Fahrenheit}")