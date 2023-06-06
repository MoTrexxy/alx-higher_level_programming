#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    print("{:s}".format(chr(i)), end="")
__________________________________________

Task 3

#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if chr(a) != 'e' and chr(a) != 'q':
        print("{:c}".format(a), end='')
