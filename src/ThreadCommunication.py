# we can communicate between threads with Event
import time
import random
import threading
from threading import Thread

CAPACITY = 5
items = []
event = threading.Event()


class Producer(Thread):

    def __init__(self, nums):
        Thread.__init__(self)
        self.nums = nums

    def run(self):

        while True:
            if len(self.nums) == CAPACITY:
                event.set()

            if not event.is_set():
                time.sleep(0.1)
                self.nums.append(random.randint(1, 100))
                print('Producer: ' + str(self.nums) + '\n')


class Consumer(Thread):

    def __init__(self, nums):
        Thread.__init__(self)
        self.nums = nums

    def run(self):

        while True:
            if len(self.nums) == 0:
                event.clear()

            if event.is_set():
                time.sleep(0.1)
                self.nums.pop()
                print('Consumer: ' + str(self.nums) + '\n')


if __name__ == '__main__':
    producer = Producer(items)
    consumer = Consumer(items)

    producer.start()
    consumer.start()


