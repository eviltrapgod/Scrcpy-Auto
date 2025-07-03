from module import mode_selector, run_module

from config import START_ASCII, END_MSG

import time

def main():
    print(START_ASCII)
    show_command = bool(input("Do you want to show the command? (y/n): ").strip().lower() == "y")
    while True:
        selected_mode = mode_selector.start_select(show_command)
        if selected_mode == 0:
            user_command = mode_selector.select_user_command()
            run_module.run_scrcpy(selected_mode, user_command)
        elif selected_mode != 0:
            run_module.run_scrcpy(selected_mode, None)
        time.sleep(1)
        print(END_MSG )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program stopped via Ctrl+C, Goodbye!")
        time.sleep(2)
else:
    print("This module is not meant to be imported")
