try:
    a = 'My name is Joe'
    b = 10
    a + b
# so here we catch the error that has been raised in the try block
except TypeError as error:
    print('TypeError: ' + str(error))
# this finally block is going to be executed whether there is an error or not
finally:
    print('This is going to be executed no matter what ...')

print("Doing some other important operations ...")
