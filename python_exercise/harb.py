while True:
    player_name = input("Enter player: ")
    health = 100
    location = "Atlantis"


    print(f"Hi {player_name}, Welcome to {location}! Your health is {health}.")

    
    while True:
        choice = input("Do you wanna go to the land(x) or explore the ocean(y)? (type 'quit' to exit): ")
    
        if choice == "quit":
            print("Thanks for playing!")
            break
        elif choice == 'x':
            print("You died of dehydration.")
            print("The End.")
            break
        elif choice == 'y':
            print("You found a magical trident!")
            health += 20
            print(f"Your health is now {health}.")
        else:
            print("Invalid choice.")
    if choice.lower() == "quit":
        break
    
    while True:    
        choice = input("Hunt the Megalodon(x) or fight Poseidon(y)? (type 'quit' to exit): ").lower()
    
        if choice == "quit":
            print("Thanks for playing!")
            break
        elif choice == 'x':
            print("You killed the Megalodon but lost some health.")
            health -= 50
            print(f"Your health is now {health}.")
        elif choice == 'y':
            print("You lost to Poseidon and barely escaped.")
            health -= 70
            print(f"Your health is now {health}.")
        else:
            print("Invalid choice.")  
    
    print("The End.")