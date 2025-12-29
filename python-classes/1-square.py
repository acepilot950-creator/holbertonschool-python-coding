#!/usr/bin/python3
"""This module defines a Square class with size validation."""


class Square:
    """This class defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a Square instance with optional size validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
