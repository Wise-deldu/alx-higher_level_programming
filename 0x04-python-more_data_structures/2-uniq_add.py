#!/usr/bin/python3

def uniq_add(my_list=[]):
    numbers = set()
    for number in my_list:
        if number not in numbers:
            numbers.add(number)

    output = sum(numbers)
    return output
