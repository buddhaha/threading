from concurrent.futures import ThreadPoolExecutor
import time

# 1.) it is not that convenient to create 100 thread
# 2.) it is quite expensive operation to create and destroy threads
#            Pools are not going to destroy threads: they will reuse them


def square(x):
    time.sleep(2)
    return x*x


nums = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=5) as executor:
    for value in nums:
        result = executor.submit(square, value)
        print(result.result())

