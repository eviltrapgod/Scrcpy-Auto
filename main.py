from module import mode_selector, run_module

from config import START_ASCII


def main():
    print(START_ASCII)
    while True:
        selected_mode = mode_selector.start_select()
        if selected_mode == 0:
            user_command = mode_selector.select_user_command()
            run_module.run_scrcpy(selected_mode, user_command)
        elif selected_mode != 0:
            run_module.run_scrcpy(selected_mode, None)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Process interrupted via Ctrl+C") 
else:
    print("This module is not meant to be imported")
