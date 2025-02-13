guests = int(input("Enter amount of guest: "))
chairs = int(input("Enter amount of chairs: "))

def calculate_arrangements():
    result = 1
    for i in range(chairs):
        result *= (guests - i)
    return result 
print("Number of possible arrangements:", calculate_arrangements())