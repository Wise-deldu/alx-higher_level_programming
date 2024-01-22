#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    multiples = []
    for i in my_list:
        if i % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return multiples
