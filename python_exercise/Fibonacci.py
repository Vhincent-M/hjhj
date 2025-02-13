import math
nth_term = int(input("Enter the number of term: "))

def fibonacci(nth_term):
    fib_seq = []
    a, b = 0, 1
    for _ in range(nth_term):
        fib_seq.append(a)
        a,b = b,a+b
    return fib_seq

fib_series = fibonacci(nth_term)
print(f"Fibonacci series: {fib_series}")

def property_one(n):
    return sum(fibonacci(n+10)[-10:]) % 11 == 0

print(f"Sum of any ten consecutive Fibonacci numbers is divisible by 11: {property_one(nth_term)}")