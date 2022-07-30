import threading
import time
"""
A lock has two state: locked or unlocked
It is created in the unlocked state.
When the state is unlocked, acquire() changes the state to locked and returns immediately. 
When the state is locked, acquire() blocks until a call to release() in another thread changes it to unlocked, 
then the acquire() call resets it to locked and returns. The release() method should only be called in the locked state; 
it changes the state to unlocked and returns immediately. If an attempt is made to release an unlocked lock, a RuntimeError will be raised.
"""



lock = threading.Lock()

def A():
   time.sleep(2)
   lock.acquire()
   print("A") 
   lock.release()



   
def B():
    lock.acquire()
    print("B")
    lock.release()
    
    
t1 = threading.Thread(target=A)
t2 = threading.Thread(target=B)

t1.start()
t2.start()

