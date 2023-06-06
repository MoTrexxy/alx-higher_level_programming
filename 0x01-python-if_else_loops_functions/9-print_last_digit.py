#!/usr/bin/python3
def print_last_digit(number):
    ef = 0
    if number < 0:
        number *= -1
    ef = 1
    last = number % 10
    if ef == 1:
        number *= -1
    print("{:d}".format(last), end="")
    return last
