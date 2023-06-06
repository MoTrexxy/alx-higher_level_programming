#!/usr/bin/python3
def uppercase(str):
    for m in str:
        if ord(m) >= ord('a') and ord(m) <= ord('z'):
            m = chr(ord(m) - 32)
    print("{:s}".format(m), end="")
    print()
