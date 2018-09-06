import _thread
import threading
from time import sleep
import Utility

#############################################################################################
Utility.run = True
# Alt
_thread.start_new_thread(Utility.print_time, ("Thread-1", 1,))  # Threads starten
#_thread.start_new_thread(Utility.print_time, ("Thread-2", 3,))

########################################
# Neu
thread = threading.Thread(target=Utility.print_time, args=("Thread-2", 3,))
Utility.threads.append(thread)
thread.start()
########################################

i = 0
while i < 5:
    i = i + 1
    sleep(1)
print("Ende")
Utility.run = False

