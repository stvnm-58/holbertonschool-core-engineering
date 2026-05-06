#!/usr/bin/env python3

def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            char_majuscule = chr(ord(i) - 32)
            print(char_majuscule, end="")
        else:
            print(i, end="")
    