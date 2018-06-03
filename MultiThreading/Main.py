import _thread
import  threading
import time
import Utility

#############################################################################################
#Alt
_thread.start_new_thread(Utility.print_time, ("Thread-1", 1,)) # Threads starten

########################################
#Neu
thread = threading.Thread(target=Utility.print_time(), args=("Thread-2", 3,))
Utility.threads.append(thread)
thread.start()

########################################

i = 0
while i < 5:
   i = i + 1
   time.sleep(1)
