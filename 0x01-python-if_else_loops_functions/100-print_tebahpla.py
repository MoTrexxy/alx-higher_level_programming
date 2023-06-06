#!/usr/bin/python3
for m in range(ord('z'), ord('a') - 1, -1):
    if m % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(m - diff)), end='')
