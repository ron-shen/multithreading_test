import threading

def A(condition):
    #with equivalent to
    # condition.acquire()
    # try:
    #     # do something...
    # finally:
    #     condition.release()    
    with condition:
        print("A")
        condition.notify_all()
    
    
def B(condition):
    with condition:
        condition.wait()
        print("B")
    
#the condition object here is used to signal threads
#one or more threads can wait (wait()) on it to get signalled (notify())
condition = threading.Condition()

t1 = threading.Thread(target=A, args=(condition,))
t2 = threading.Thread(target=B, args=(condition,))

#the order here is important because we have to hit condition.wait first
#otherwise, t1 notifies nothing
t2.start()
t1.start()
