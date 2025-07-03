from config import COMMAND_DICT

import time 
import os


# Функция для запуска scrcpy с заданным режимом,
# переданным через аргумент selected_mode
def run_scrcpy(selected_mode, user_command=None):
    if selected_mode == 0:
        time.sleep(0.4)
        print("launch scrcpy")
        time.sleep(0.4)
        print("Almost...")
        time.sleep(0.3)
        os.system(f"scrcpy {user_command}") 
        time.sleep(0.5)
        print("Command executed with key!")
        time.sleep(0.7)
    elif selected_mode != 0:
        # attempt to run scrcpy with the selected mode
        try:
            time.sleep(0.4)
            print("launch scrcpy")
            time.sleep(0.4)
            print("Almost...")
            time.sleep(0.3)
            command = COMMAND_DICT[selected_mode]["command"]
            os.system(f"scrcpy {command}")
            time.sleep(0.5)
            print("Command executed with key!")
            time.sleep(0.7)
            # Handling incorrectly entered key
        except KeyError:
            print("Invalid mode selected, please choose correct mode.")
            # End of program execution
        finally:
            print("Done! You can use other modes")
