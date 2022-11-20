
result = None

while True:
    try:
        result = input("Please, enter a number: ")
        result = int(result)
        break
    except ValueError:
        print("This is not a valid number...")


print("The value of the result is: " + str(result))



