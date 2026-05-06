#!/usr/bin/env python3

for a in range(0, 10):
    for b in range(0, 10):
        if a >= b:
            continue
        print("{}{}".format(a, b), end="")
        if a != 8:
            print(', ',end="")
        else:
            print()
        