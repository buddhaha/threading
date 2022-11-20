import threading
from threading import RLock


class Test:

    def __init__(self):
        self.num1 = 1
        self.num2 = 2
        self.lock = RLock()

    def increment_first(self):
        with self.lock:
            self.num1 += 1

    def increment_second(self):
        with self.lock:
            self.num2 += 1

    def increment_both(self):
        with self.lock:
            self.increment_first()
            self.increment_second()






