#!/usr/bin/env python3

for a in range(0 , 9):
    for b in range(0 , 9):
        print("{}{}".format(a, b), end="")
        if a != 9 and b != 9:
            print(", ", end="")
