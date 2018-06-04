from time import sleep
import logging

threads = []
run = True

#############################################################################################
# Thread Functions
def print_time(threadName, delay):
    while run:
        sleep(delay)
        print(str(threadName))
        # logging.warning(threadName)
