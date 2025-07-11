import logging

from time import time, sleep

from data import config
from services import input_service
from services import output_service

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='scrcpy_auto.log',
    filemode='a'
    )

def main():
    output_service.print_start_screen()
    pass

if __name__ == "__main__":
    main()
