#!/usr/bin/env python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    return max(a_dictionary.get, key=a_dictionary.get)
