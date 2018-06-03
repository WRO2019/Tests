import time
import logging

threads = []

#############################################################################################
# Thread Functions
def print_time(threadName, delay):
    while True:
        logging.warning(threadName)
        time.sleep(delay)
