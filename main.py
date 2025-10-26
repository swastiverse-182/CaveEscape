import random

def cave_escape():
    print("=== Cave Escape Game ===")
    print("Find the treasure without meeting the monster.\n")

    # Get total rooms from user
    while True:
        try:
            total_rooms = int(input("Enter the number of rooms: "))
            if total_rooms < 2:
                print("There should be at least 2 rooms.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Get number of attempts from user
    while True:
        try:
            max_attempts = int(input("Enter the number of attempts allowed: "))
            if max_attempts < 1:
                print("You need at least 1 attempt.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Game setup
    rooms = list(range(1, total_rooms + 1))
    treasure_room = random.choice(rooms)
    monster_room = random.choice([r for r in rooms if r != treasure_room])

    print(f"\nThere are {total_rooms} rooms numbered 1 to {total_rooms}.")
    print("One has treasure, one has a monster.\n")

    # Game loop
    for attempt in range(1, max_attempts + 1):
        try:
            choice = int(input(f"Attempt {attempt}/{max_attempts} - Choose a room (1-{total_rooms}): "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if choice < 1 or choice > total_rooms:
            print(f"Room number must be between 1 and {total_rooms}.")
            continue

        if choice == treasure_room:
            print("You found the treasure! You win!")
            break
        elif choice == monster_room:
            print("You met the monster. You lose.")
            break
        else:
            print("The room is empty. Try another.")

    else:
        print(f"Game over. The treasure was in room {treasure_room} and the monster was in room {monster_room}.")

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        print("\nStarting a new game...\n")
        cave_escape()
    else:
        print("Thanks for playing.")

# Start the game
cave_escape()