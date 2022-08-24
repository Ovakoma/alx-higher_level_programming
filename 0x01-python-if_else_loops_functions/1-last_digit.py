#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
check = 0
if (n < 0):
    n *= -1
    check = 1
last_d = n % 10
if (check):
    last_d *= -1
    n *= -1
if (last_d > 5):
    print("Last digit of %d is %d and is greater than 5" % (n, last_d))
elif (last_d == 0):
    print("Last digit of %d is %d and is 0" % (n, last_d))
elif (last_d < 6 and last_d != 0):
    print(f"Last digit of {n:d} is {last_d:d} and is less than 6 and not 0")
