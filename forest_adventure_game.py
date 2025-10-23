import time

def print_pause(message, delay=1.5):
    """Print a message with a short delay."""
    print(message)
    time.sleep(delay)

def intro():
    print_pause("You wake up in a dark forest 🌲...")
    print_pause("You have no idea how you got here.")
    print_pause("There are two paths ahead of you:")
    print_pause("➡️ One leads to a small village.")
    print_pause("➡️ The other goes deeper into the forest.")
    print_pause("You can also look around for clues.")

def choose_path():
    while True:
        print("\nWhat would you like to do?")
        print("1️⃣  Go to the village")
        print("2️⃣  Go deeper into the forest")
        print("3️⃣  Look around for clues")
        print("4️⃣  Quit the game")

        choice = input("> ")

        if choice == "1":
            village()
            break
        elif choice == "2":
            forest()
            break
        elif choice == "3":
            look_around()
        elif choice == "4":
            print_pause("Goodbye, brave explorer! 🏕️")
            exit()
        else:
            print("Please choose a valid option (1-4).")

def village():
    print_pause("\nYou walk along the path to the village...")
    print_pause("The houses look abandoned.")
    print_pause("Suddenly, you hear a noise behind you...")
    print_pause("A friendly villager appears! 👋")
    print_pause("They offer you food and a map to escape the forest.")
    print_pause("You thank them and follow the map out safely.")
    print_pause("🎉 YOU WIN! You escaped the forest alive.")
    play_again()

def forest():
    print_pause("\nYou wander deeper into the forest...")
    print_pause("The trees become thicker, and the light fades...")
    print_pause("You hear growling nearby... 🐺")
    print_pause("A wild wolf jumps out!")
    fight_or_run()

def fight_or_run():
    while True:
        print("\nDo you want to:")
        print("1️⃣  Fight the wolf")
        print("2️⃣  Run away")
        choice = input("> ")

        if choice == "1":
            print_pause("You grab a stick and face the wolf...")
            print_pause("The wolf snarls and leaps — but you dodge and scare it off!")
            print_pause("You're safe... for now.")
            print_pause("You find a hidden cave nearby and rest.")
            print_pause("🏆 You survived the night!")
            play_again()
            break
        elif choice == "2":
            print_pause("You sprint back toward the start...")
            print_pause("You're exhausted but safe.")
            choose_path()
            break
        else:
            print("Please choose 1 or 2.")

def look_around():
    print_pause("\nYou look around carefully...")
    print_pause("You find a shiny sword on the ground! ⚔️")
    print_pause("You might need this later...")
    choose_path()

def play_again():
    while True:
        replay = input("\nWould you like to play again? (yes/no): ").lower()
        if replay in ["yes", "y"]:
            print_pause("\nRestarting the game...\n")
            start_game()
            break
        elif replay in ["no", "n"]:
            print_pause("Thanks for playing! 👋")
            exit()
        else:
            print("Please type 'yes' or 'no'.")

def start_game():
    intro()
    choose_path()

if __name__ == "__main__":
    start_game()
