from data import config

import os
import logging

logger = logging.getLogger(__name__)

def print_start_screen():
    print(config.START_ASCII)






if __name__ == "__main__":
    logging.error("USER RUN MODULE DIRECTLY")
    logging.info("raise RuntimeError. Program has been stopped.")
    raise RuntimeError("This is a service module and cannot be run directly.")
else:
    pass
