#!/usr/bin/env python3

def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as f:
        return write(text)