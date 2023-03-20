# Liskov Substitution Principle. (LSP)


class Rectangle:
    def __init__(self, width, height):
        """height and width become private propeties
        as opposed to exposed attributes"""
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"

    # Getters and Setters

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f"Expected an area of {expected}, got {rc.area}")


rc = Rectangle(2, 3)
use_it(rc)

# All good with the above, now let us try to break it
# by breaking the Liskov Substitution method by making a derived class (i.e. inherits from Rectangle)
# which absolutely does not work with the use_it() method.
# and in the process see why we used properties as opposed to attributes.


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


sq = Square(5)
use_it(sq)

# The "problem" is with line 39 (rc.height = 10), because it changes both the width and the height to 10.
# This is a direct violation of the Liskov substitution principle which states that
# whenever you have an interface taking some sort of base class,
# you should be able to stick in any of its inheriters
# (e.g. if you take a Rectangle as a base class, you should be able to stick in a square)
# and everything should work correctly

# There are many ways of correcting this problem:
# one could argue that there is no need for a Square class in the first place,
# you could have a boolean property in the Rectangle class that states whether it's a Square or not,
# or you could have a Factory method which could make a square instead of a Rectangle.
