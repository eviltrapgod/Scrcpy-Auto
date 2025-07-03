import time

from config import COMMAND_DICT


def start_select():
    print("Available modes:")
    for number, info in COMMAND_DICT.items():
        print(f"{number}: {info['desc']} — ({info['command']})")
        time.sleep(0.07)
    selected_mode = int(input("Select mode: "))
    return selected_mode

def select_user_command():
    user_command = input("Enter your command: ")
    return user_command
