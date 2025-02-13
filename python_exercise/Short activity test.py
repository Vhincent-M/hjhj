player_name = input("Enter your name: ")
health = 100
location = "forest"

health -= 20  # player loses health
print(f"{player_name}, your health is now {health}.")

def show_status(name, health, location):
    print(f"{name}, you are in the {location} with health {health}.")

show_status(player_name, health, location)

choice = input("You see a wolf. Do you fight (f) or run (r)? ")
if choice == 'f':
    health -= 30
    print("You chose to fight and lost some health.")
elif choice == 'r':
    print("You chose to run away safely.")
else:
    print("Invalid choice.")
show_status(player_name, health, location)