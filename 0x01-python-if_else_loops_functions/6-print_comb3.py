#!/usr/bin/python3
for num in range(10):
    for num2 in range(10):
        if num < num2:
            print("{}{}".format(num, num2), end='')
            if num < 8:
                print(", ", end='')
print()
