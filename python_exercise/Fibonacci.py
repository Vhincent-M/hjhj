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

import math
def property_two(a, b):
    return math.gcd(a, b) == 1

def verify_prop_two(n):
    fib_s = fibonacci(n)
    return all(property_two(fib_s[i], fib_s[i+1]) for i in range(len(fib_s)-1))

print(f"Consecutive Fibonacci Numbers are Co-prime: {verify_prop_two(nth_term)}")

def property_three(n):
    fib_s = fibonacci(n+2)
    return sum(fib_s[:n]) == fib_s[n+1] - 1

print(f"Sum of first {nth_term} Fibonacci numbers equals F(n+2) - 1: {property_three(nth_term)}")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def property_four(n):
    fib_s = fibonacci(n)
    return [fib_s[i] for i in range(4, len(fib_s), 2) if not is_prime(fib_s[i])]

print(f"Fibonacci numbers in composite positions that are composite: {property_four(nth_term)}")