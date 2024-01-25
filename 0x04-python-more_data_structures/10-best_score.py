#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        a = list(a_dictionary.values())
        b = list(a_dictionary.keys())
        return b[a.index(max(a))]
