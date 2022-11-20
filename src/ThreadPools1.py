from concurrent.futures import ThreadPoolExecutor
import time

# 1.) it is not that convenient to create 100 thread
# 2.) it is quite expensive operation to create and destroy threads
#            Pools are not going to destroy threads: they will reuse them


def operation():
    time.sleep(3)
    print('The operation is finished...')


with ThreadPoolExecutor(max_workers=4) as executor:
    executor.submit(operation)
    executor.submit(operation)
    executor.submit(operation)
    executor.submit(operation)

print('Finished with the tasks...')
