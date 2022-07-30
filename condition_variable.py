import threading

def A(condition):
    #with equivalent to
    # condition.acquire()
    # try:
    #     # do something...
    # finally:
    #     condition.release()
    print("in a")    
    with condition:
        print("A")
        condition.notify_all()


   
def B(condition, t1):
    print("in b")  
    with condition:
        #it ensures that wait() run first
        #because thread t2 acquire the lock first,
        #it relases the lock after calling wait(),
        #so then thread t1 can acquire the lock to do something 
        t1.start()
        condition.wait()
        print("B")
    
#the condition object here is used to signal threads
#one or more threads can wait (wait()) on it to get signalled (notify())
condition = threading.Condition()

t1 = threading.Thread(target=A, args=(condition,))
t2 = threading.Thread(target=B, args=(condition, t1))

t2.start()

