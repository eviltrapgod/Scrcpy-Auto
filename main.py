from module import mode_selector, run_module

from config import START_ASCII


def main():
    while True:
        print(START_ASCII)
        selected_mode = mode_selector.start_select()
        run_module.run_scrcpy(selected_mode)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Process interrupted via Ctrl+C") 
else:
    print("This module is not meant to be imported")
