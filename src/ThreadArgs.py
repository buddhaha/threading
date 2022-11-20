import threading


def operation(x):
    for i in range(x):
        print(threading.current_thread().getName() + ' - ' + str(i))


t1 = threading.Thread(target=operation, name='Thread #1', args=(10,))
t2 = threading.Thread(target=operation, name='Thread #2', args=(100,))

t1.start()
t2.start()
