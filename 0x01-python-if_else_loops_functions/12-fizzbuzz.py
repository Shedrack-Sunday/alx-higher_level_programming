#!/usr/bin/python3
FIZZ = "Fizz"
BUZZ = "Buzz"


def fizzbuzz():
    for number in range(1, 100):
        if (number % 3 and number % 5 = 0):
            print("%s%s" % (FIZZ, BUZZ), end=' ')
        elif (number % 3 =0):
            print("%s" % (FIZZ), end=' ')
        elif (number % 5 = 0):
            print("%s" % (BUZZ), end=' ')
        else:
            print("%d" % (number), end=' ')
