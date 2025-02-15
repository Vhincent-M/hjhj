while True:
    player_name = input("Enter player: ")
    health = 100
    location = "Atlantis"


    print(f"Hi {player_name}, Welcome to {location}! Your health is {health}.")

    
    while True:
        choice = input("Do you wanna go to the land(x) or explore the ocean(y)? (type 'quit' to exit): ")
    
        if choice == "quit":
            print("Thanks for playing!")
            exit()  
        elif choice == 'x':
            print("\nYou died of dehydration.")
            print("The End.")
            break  
        elif choice == 'y':
            print("\nYou found a magical trident!")
            health += 20
            print(f"Your health is now {health}.")
            break 
        else:
            print("Invalid choice. Please choose 'x' or 'y'.")
    
    if choice == 'x':
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
        else:
            continue
    
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
            
    while True:    
        choice = input("Seek help from Aquaman(x) or Namor(y)? (type 'quit' to exit): ").lower()
    
        if choice == "quit":
            print("Thanks for playing!")
            break
        elif choice == 'x':
            print("Aquaman handed you an Atlantean armor. You gained 50 health.")
            health += 50
            print(f"Your health is now {health}.")
        elif choice == 'y':
            print("Namor killed you just because he wanted to.")
            print("The End.")
        
        else:
            print("Invalid choice.")
            continue 

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
    
    print("The End.")