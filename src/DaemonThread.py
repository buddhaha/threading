import threading

# PVM (python Virtual Machine) creates the MainThread
# daemon threads are terminated if all other normal threads finish execution
# BUT the Python is not terminates if at least 1 normal thread is running


def normal_operation():
    for _ in range(1000000):
        print('Normal thread is running...')


def daemon_operation():
    while True:
        print('Daemon thread is running...')


t1 = threading.Thread(target=normal_operation, name="Normal Thread #1")
t2 = threading.Thread(target=daemon_operation, name="Daemon Thread", daemon=True)

t1.start()
t2.start()
