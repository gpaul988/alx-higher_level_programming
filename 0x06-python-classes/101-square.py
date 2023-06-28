#!/usr/bin/python3
# Graham S. Paul (101-square.py)
"""Explains class square"""


class Square:
    """Shows a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Boot fresh square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Acquire contemporary size of square"""
        return self.__size

    @property
    def position(self):
        """Acquire contemporary position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Calibrate contemporary position of square"""
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        """Calibrate contemporary size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Restores contemporary area of square"""
        return self.__size ** 2

    def my_print(self):
        """Pulls square using # considering the position"""
        if not self.size:
            print()
            return

        print("\n" * self.position[1], end="")
        print("\n".join([" " * self.position[0] +
                        "#" * self.size
                         for i in range(self.size)]))

    def __str__(self):
        """Explains print() representation of the square"""
        return f"" if not self.size else (
                f"\n" * self.position[1] +
                f"\n".join([" " * self.position[0] +
                            "#" * self.size
                            for i in range(self.size)]))
