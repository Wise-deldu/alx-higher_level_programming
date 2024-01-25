#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    final_dictionary = {}
    for key, value in a_dictionary.items():
        final_dictionary[key] = value * 2
    return final_dictionary
