n = int(input("Enter the number of terms : "))
fib_series = [0,1]
while len(fib_series) < n:
    fib_series.append(fib_series[-1] + fib_series[-2])
print(f"Fibonacci series up to {n} terms : {fib_series}")