#!/usr/bin/python3

for alpha in range(ord('Z'), ord('A') - 1, -1):
    if alpha % 2 == 0:
        print(chr(alpha + 32), end="")
    else:
        print(chr(alpha), end="")
