#!/usr/bin/env python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or len(my_list) <= idx:
        return None
    
    my_list[idx] = element

    return my_list
