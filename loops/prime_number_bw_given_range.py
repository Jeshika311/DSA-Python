start = int(input("Enter the starting number of the range : "))
end = int(input("Enter the ending number of the range : "))

for num in range(start , end+1):
    is_prime = True

    for i in range(2 , int(num**0.5)+1):
        if num%i==0:
            is_prime = False
            break

    if is_prime and num>1:
        print(num)