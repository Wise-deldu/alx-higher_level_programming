#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    return sum([mul(a[0], a[1]) for a in my_list]) / sum(a[1] for a in my_list)


def mul(a, b):
    return a * b
