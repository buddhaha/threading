import threading
import random
import time

# HPC clusters - of course the capacity is limited
# only 5 users can acquire the cluster at the same time

semaphore = threading.Semaphore(10)
operation_counter = 0


def compute():
    global operation_counter
    semaphore.acquire()
    print('Performing heavy computation on the cluster...')
    operation_counter += 1
    print('Total number of computations: ' + str(operation_counter))
    # the given thread will sleep for a random amount of time [3sec - 8sec]
    time.sleep(random.randint(3, 8))
    print('Finished computation...')
    semaphore.release()
    operation_counter -= 1
    print('Total number of computations: ' + str(operation_counter))


while True:
    time.sleep(0.1)
    t = threading.Thread(target=compute)
    t.start()
