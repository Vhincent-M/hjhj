while True:
    try:
        num = int(input("Enter a number a number greater than or equal to 2: "))
        if num < 2:
            print("Please enter a number greater than or equal to 2.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def check_sum(num):
    for i in range(2, num):
        if is_prime(i) and is_prime(num - i):
            return i, num - i
    return None

result = check_sum(num)
if result:
    print(f"{num} = {result[0]} and {result[1]}.")
else:
    print(f"{num} cannot be expressed as the sum of two prime numbers.")