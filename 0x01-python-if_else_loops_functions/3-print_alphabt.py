#!/usr/bin/python3

for lower_alpha in range(ord('a'), ord('z') + 1):
    if chr(lower_alpha) != 'q' and chr(lower_alpha) != 'e':
        print("{}".format(chr(lower_alpha)), end="")
