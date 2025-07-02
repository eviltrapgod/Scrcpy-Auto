import time 
import os

from config import COMMAND_DICT



def run_scrcpy(selected_mode):
    time.sleep(0.3)
    print("Запуск scrcpy")
    time.sleep(0.3)
    print("Почти...")
    os.system(f"scrcpy {COMMAND_DICT[selected_mode]}")
    print("выполнена команда с ключем")
    time.sleep(0.6)
    print("Готово! Можете использовать другие режимы.")
    # дальше некст итерация программы
