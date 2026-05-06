#!/usr/bin/env python3

for code in range(97, 123):
    lettre = chr(code)

    if lettre == 'q' or lettre == 'e':
        continue
    
    print("{}".format(lettre), end="")

print()
