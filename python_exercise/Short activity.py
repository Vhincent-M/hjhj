player_name = input("Enter your name: ")
health = 100
location = 'in another world'

print(f"Hello {player_name}, you just woke up in a different world! You now have {health} health points. Throughout this challenge, you'll face various scenarios, and your decisions will impact your health, either increasing or decreasing it.")

def show_status(name, health, location):
    print(f"{name}, you are {location} with health {health}.")

show_status(player_name, health, location)

# Scenario 1: Slime encounter
choice = input("\nYou see a slime. Do you fight (f) or run (r)? ")
if choice == 'f':
    health -= 30
    print("You put up a good fight and lost some health (-30 health).")
elif choice == 'r':
    print("You chose to run away safely.")
else:
    print("Invalid choice.")

show_status(player_name, health, location)

# Scenario 2: The path
print("\nYou saw a pathway that might lead you to a nearby town.")
choice = input("Do you take the pathway (p) or choose your own route (r)? ")
if choice == 'p':
    print("You are now headed to Foosha Village.")
elif choice == 'r':
    health -= 5
    print("You chose to go your own route and tripped by an unexpected rock (-5 health).")
    print("You still decided to just take the pathway.")
else:
    print("Invalid choice.")

show_status(player_name, health, location)

# Scenario 3: Another traveler
print("\nWhile on your way to the village you encountered another traveler heading that way.")
print("Note: You are starting to get hungry")

choice = input("Do you talk to the traveler? (y) or (n) ")
if choice == 'y':
    health += 10
    print("You chose to talk to the traveler")
    print("The traveler seemed to like you and gave you an apple (+10 health)!")
elif choice == 'n':
    health -= 15
    print("You chose to mind your business and now you're starving (-15 health).")
else:
    print("Invalid choice.")

show_status(player_name, health, location)

# Scenario 4: Foosha Village
print("\nYou've just arrived at Foosha Village")

choice = input("You now have the option to find your self an inn (i) or enjoy the rest of the night by finding a pub (p). What do you choose? ")
if choice == 'i':
    health += 20
    print("You chose to find your self an inn (+20 health).")
elif choice == 'p':
    health -= 10
    print("You chose to enjoy the rest of the night by finding a pub and got yourself drunk (-10 health).")
else:
    print("Invalid choice.")

show_status(player_name, health, location)

# Scenario 5: The Mysterious Figure
print("\nAs you leave Foosha Village, you encounter a mysterious figure cloaked in shadows.")
choice = input("Do you approach the figure (a) or avoid them (v)? ")

if choice == 'a':
    print("You approach the mysterious figure.")
    if health > 50:
        health -= 10
        print("The figure challenges you to a duel! Though you fight bravely, you are slightly injured (-10 health).")
    else:
        health += 20 
        print("The figure senses your weakness and offers you a healing potion! (+20 health).")

elif choice == 'v':
    print("You decide to avoid the mysterious figure.")
    print("You feel a sense of unease, but nothing bad happens.")

else:
    print("Invalid choice.")

show_status(player_name, health, location)

print("Your adventure continues...")