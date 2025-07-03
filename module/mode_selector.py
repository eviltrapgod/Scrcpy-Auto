import time

from config import COMMAND_DICT


def start_select(show_command):
    try:
        if show_command:
            print("Available modes:")
            for number, info in COMMAND_DICT.items():
                print(f"{number}: {info['desc']} — ({info['command']})")
                time.sleep(0.07)
            selected_mode = int(input("Select mode: "))
            return selected_mode
        elif not show_command:
            print("Available modes:")
            for number, info in COMMAND_DICT.items():
                print(f"{number}: {info['desc']} ")
                time.sleep(0.07)
            selected_mode = int(input("Select mode: "))
            return selected_mode
    except ModuleNotFoundError:
        print(""" 
            DO NOT RUN THIS FILE, IT'S MODULE, RUN - main.py
            DO NOT RUN THIS FILE, IT'S MODULE, RUN - main.py
            DO NOT RUN THIS FILE, IT'S MODULE, RUN - main.py
            """)
        time.sleep(5)

def select_user_command():
    user_command = input("Enter your command: ")
    return user_command
