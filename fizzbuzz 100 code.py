for int in range(1, 101):
    if int % (3 * 5) == 0:
        print("Fizzbuzz")
    elif int % 5 == 0:
        print("Buzz")
    elif int % 3 == 0:
        print("Fizz")
    else:
        print (int)