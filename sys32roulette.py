import os
import sys
import random
import ctypes

system32_path = "C:\\Windows\\System32"

# Check for admin rights and relaunch as admin if needed
def run_as_admin():
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        is_admin = False
    if not is_admin:
        print("Requesting administrator privileges...")
        # Relaunch the script with admin rights
        params = ' '.join([f'"{arg}"' for arg in sys.argv])
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        except Exception as e:
            print(f"Failed to elevate privileges: {e}")
        sys.exit()

run_as_admin()

def main():
    print("Welcome to windows system32 roulette!")
    print("NOTE: anything caused by running this program is not the fault of the creator, as the runner has multiple chances to opt out, has downloaded and run the file by choice, and knows what it does.")
    if input("WARNING!!! \n Are you sure you want to play? This may delete important system files. (y/n): ").lower() != 'y':
        print("Exiting...")
        sys.exit()
    else:
        if input("FINAL WARNING!!! \n RUNNING THIS *WILL* MOST LIKELY DO IRRIVERSABLE DAMAGE TO YOUR DEVICE.  \n ONLY RUN IN A VIRTUAL MACHINE OR DEVICE YOU DO NOT CARE ABOUT!!! \n I understand the risks, and would like to go ahead with the program. (y/n): ").lower() != 'y':
            print("Exiting...")
            sys.exit
        else:
            pass
    print("Starting the game...")
    # Only select regular files
    files = [f for f in os.listdir(system32_path) if os.path.isfile(os.path.join(system32_path, f))]
    if not files:
        print("No regular files found in System32 directory.")
        sys.exit()
    random_file = random.choice(files)
    full_path = os.path.join(system32_path, random_file)
    print(f"Your random system32 file is: {random_file}")
    print(f"Full path: {full_path}")
    print(f"We will now get a random number between 1 and 6.  If you get a 1, we will delete this file.")
    random_number = random.randint(1, 6)
    print(f"You rolled a {random_number}.")
    if random_number == 1:
        try:
            os.remove(full_path)
            print(f"{random_file} has been deleted.")
        except Exception as e:
            print(f"Failed to delete {random_file}: {e}")
    else:
        print(f"{random_file} has not been deleted.")
    if input("Do you want to play again? (y/n): ").lower() == 'y':
        main()
    else:
        print("Thanks for playing!")
        sys.exit()

if True:
    main()



