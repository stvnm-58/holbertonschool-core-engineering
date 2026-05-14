#!/usr/bin/env python3

class Rectangle:
    def __init__(self, width, height):
        
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height
    
    def __str__(self):
        return f"rectangle {self.__width}/{self.__height}"
