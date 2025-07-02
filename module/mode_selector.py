from config import COMMAND_DICT
def start_select():
    print("Available modes:")
    for mode in range(1, 21):
        print(f"Mode {mode}: {COMMAND_DICT[mode]}")
        selected_mode = int(input("Select mode: "))
        return selected_mode
