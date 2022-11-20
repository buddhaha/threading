import threading
from threading import Lock

x = 0
# only a single thread may acquire the lock at the same time
# when a lock is acquired - then other threads have to wait for it to be
# accessible again
lock = Lock()


def increment():
    global x
    # the threads may get into BLOCKED state
    lock.acquire()
    # THIS IS THE CRITICAL SECTION
    x = x + 1
    lock.release()


def operation():
    for _ in range(10000000):
        increment()


t1 = threading.Thread(target=operation, name='Thread #1')
t2 = threading.Thread(target=operation, name='Thread #2')

t1.start()
t2.start()

t1.join()
t2.join()

# x = 20 million
print('The value of x: ' + str(x))
