def calculate_arrangements():
    result = 1
    for i in range(chairs):
        result *= (guests - i)
    return result


while True:
    try:
        guests = int(input("Enter the number of guests: "))
        chairs = int(input("Enter the number of chairs: "))
        break
    except ValueError:
        print("Invalid input: Please enter valid integers for guests and chairs.")


print("Number of possible arrangements:", calculate_arrangements())