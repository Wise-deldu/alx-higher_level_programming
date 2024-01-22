#!/usr/bin/python3

def no_c(my_string):
    final_string = ""
    remove_char = ['c', 'C']
    
    for i in my_string:
        if i not in remove_char:
            final_string += i
    return final_string
