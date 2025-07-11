from data import commands
import json

import logging
logger = logging.getLogger(__name__)

import sys


def request_to_display_commands():
    user_selection = input("Display the commands themselves in their list? (Looks worse): ")
    if user_selection.strip().lower() in ["yes", "y", "true", "1"]:
        logging.info("User chose to display commands.")
        return True
    elif user_selection.strip().lower() in ["no", "n", "false", "0"]:
        logging.info("User chose not to display commands.")
        return False
    else:
        logging.warning("Invalid input received.")
        print("Please enter yes or no :з")
        return request_to_display_commands()

def select_command():
    pass

def get_json_command_list(): 
    json_command_list = input("Выберете json файл с командами:")
    return json_command_list








if __name__ == "__main__":
    logging.error("User run module directly")
    logging.warning("raise RuntimeError. Program has been stopped.")
    raise RuntimeError("This is a service module and cannot be run directly.")
else:
    pass
