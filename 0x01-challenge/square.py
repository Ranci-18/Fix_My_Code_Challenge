#!/usr/bin/python3
"""class square module"""


class Square():
    """class square"""
    def __init__(self, width=0, height=0):
        """init method"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PerimeterOfMySquare(self):
        """Perimeter of square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation
        of object to print"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimeterOfMySquare())
