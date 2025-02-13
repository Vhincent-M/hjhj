def fibonacci(terms):
    fib_sequence = []
    a, b = 0, 1
    
    # Generate Fibonacci sequence
    for _ in range(terms):
        fib_sequence.append(a)
        a, b = b, a + b
    
    return fib_sequence

def sum_ten_consecutive_fib(n):
    return sum(fibonacci(n+10)[-10:]) % 11 == 0

def are_coprime(a, b):
    import math
    return math.gcd(a, b) == 1

def verify_fib_coprime(n):
    fib_seq = fibonacci(n)
    return all(are_coprime(fib_seq[i], fib_seq[i+1]) for i in range(len(fib_seq)-1))

def sum_fib_n(n):
    fib_seq = fibonacci(n+2)
    return sum(fib_seq[:n]) == fib_seq[n+1] - 1

def fib_composite_positions(n):
    fib_seq = fibonacci(n)
    return [fib_seq[i] for i in range(4, len(fib_seq), 2) if not is_prime(fib_seq[i])]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# User input
terms = int(input("Enter the number of terms to generate: "))

# Generate and print Fibonacci sequence
fib_series = fibonacci(terms)
print(f"Fibonacci series: {fib_series}")

# Property Checks
print(f"Sum of any ten consecutive Fibonacci numbers is divisible by 11: {sum_ten_consecutive_fib(terms)}")
print(f"Consecutive Fibonacci numbers are coprime: {verify_fib_coprime(terms)}")
print(f"Sum of first {terms} Fibonacci numbers equals F(n+2) - 1: {sum_fib_n(terms)}")
print(f"Fibonacci numbers in composite positions that are composite: {fib_composite_positions(terms)}")