
class LargeValueException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def message(self):
        return self.msg


class SmallValueException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def message(self):
        return self.msg


value = -10

try:

    if value < 0:
        raise SmallValueException('The value is too small...')
    elif value > 100:
        raise LargeValueException('The value is too large...')

    print('The value is within the range [0,100]...')

except SmallValueException as small:
    print(small.message())
except LargeValueException as large:
    print(large.message())

print('The application finishes execution...')
