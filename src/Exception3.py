
age = 12

try:

    if age < 18:
        raise Exception('You are underage...')

# we can create an alias for the exception with the AS keyword
except Exception as exc:
    print(exc.args[0])
