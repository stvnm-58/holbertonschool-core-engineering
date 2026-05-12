#!/usr/bin/env python3

class Square:
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError ("Size must be integer")
        if size < 0:
            raise ValueError ("size must be >= 0")
        self.__size = size
