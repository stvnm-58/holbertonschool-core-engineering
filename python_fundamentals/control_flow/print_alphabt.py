#!/usr/bin/env python3

for i in range(97, 123):
    lettre = chr(i)
    if lettre != 'q' and lettre != 'e':
        print("{}".format(lettre), end="")
