# import necessary modules or redirect to main.py
try:
    from config import COMMAND_DICT 
except ModuleNotFoundError:
    os.system("python3 main.py")

import time 
import os


# function to print text with a delay (To improve user experience)
def delay_print(text, delay=0.4):
    print(text)
    time.sleep(delay)

# Function to run scrcpy with the specified mode
def run_scrcpy(selected_mode, user_command=None):
    try:
        # run user command
        if selected_mode == 0:
            delay_print("launch scrcpy", 0.3)
            delay_print("Almost...", 0.6)
            os.system(f"scrcpy {user_command}")
            delay_print("Command executed with key!", 0.4)
        # run defoult command
        elif selected_mode != 0:
            try:
                delay_print("launch scrcpy", 0.3)
                delay_print("Almost...", 0.6)
                command = COMMAND_DICT[selected_mode]["command"]
                os.system(f"scrcpy {command}")
                delay_print("Command executed with key!", 0.4)
            # handle invalid mode number
            except KeyError:
                delay_print("Invalid mode selected, please choose correct mode.")
    # special case of module importation ;)    
    except ModuleNotFoundError:
        os.system("cd .. && python3 ./main.py")
