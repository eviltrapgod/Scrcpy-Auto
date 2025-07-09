# import necessary modules or redirect to main.py
try:
    from config import COMMAND_DICT
except ModuleNotFoundError:
    os.system("python3 main.py")

import time
import os

# Function to start mode selection
def start_select(show_command):
    try:
        # Show available modes, if user wants to see commands
        if show_command:
            print("Available modes:")
            for number, info in COMMAND_DICT.items():
                print(f"{number}: {info['desc']} — ({info['command']})")
                time.sleep(0.05)
            selected_mode = int(input("Select mode: "))
            return selected_mode
        # Show available modes without commands
        elif not show_command:
            print("Available modes:")
            for number, info in COMMAND_DICT.items():
                print(f"{number}: {info['desc']} ")
                time.sleep(0.05)
            selected_mode = int(input("Select mode: "))
            return selected_mode
        # Handle invalid mode selection
    except ValueError:
        print("UNCORRECT INPUT, ENTER MODE NUMBER!")
        return start_select(show_command)
    
# Function to select user command
def select_user_command():
    user_command = input("Enter your command: ")
    return user_command
