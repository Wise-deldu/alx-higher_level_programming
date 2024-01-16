#!/usr/bin/python3

for alp in range(ord('Z'), ord('A') - 1, -1):
    print("{}".format(chr(alp + 32) if alp % 2 == 0 else chr(alp)), end="")
