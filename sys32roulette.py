import os
import sys
import random

system32_path = "C:\\Windows\\System32"

def main():
    print("Welcome to windows system32 roulette!")
    if input("WARNING!!! \n Are you sure you want to play? This may delete important system files. (y/n): ").lower() != 'y':
        print("Exiting...")
        sys.exit()
    else:
        print("Starting the game...")
    files = os.listdir(system32_path)
    random_file = random.choice(files)
    print(f"Your random system32 file is: {random_file}")
    print(f"Full path: {os.path.join(system32_path, random_file)}")
    print(f"We will now get a random number between 1 and 6.  If you get a 1, we will delete this file.")
    random_number = random.randint(1, 6)
    print(f"You rolled a {random_number}.")
    if random_number == 1:
        os.remove(os.path.join(system32_path, random_file))
        print(f"{random_file} has been deleted.")
    else:
        print(f"{random_file} has not been deleted.")
    if input("Do you want to play again? (y/n): ").lower() == 'y':
        main()
    else:
        print("Thanks for playing!")
        sys.exit()

if True:
    main()

