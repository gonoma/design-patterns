# Open-Closed Principle
# Open for extension, Closed for modification

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# one of the requirements of this application
# is to be able to filter products by color


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

    # This approach does not scale!
    # Appart from breaking the OC Principle, you might cause
    # a "State Space Explosion".

    # // 2 --> 3 filtering by two criteria (color and size),
    # gives us at least 3 methods

    # 3 --> 7 filtering by three criteria could give you 7 methods,
    # It does not Scale!


# To solve this we can use "Enterprise Patterns", which would need a separate course,
# but here we are implementing one of them

# Specification
"""Base class 1, you are meant to override this method"""


class Specification:
    def is_satisfied(self, item):
        pass

    # Line 164, this is useful to simplify code, and can be extended
    def __and__(self, other):
        return AndSpecification(self, other)


"""Base class 2"""


class Filter:
    def filter(self, items, spec):
        pass


"""This class inherits from Specification"""


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        """determine if the item color is equal to
        the color in the specification"""
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


# Building a combinator, like in line 34:
class AndSpecification(Specification):
    """Checks that any number of speficications are applied,
    the way we are going to do this is by having a variable number of
    arguments, which are the actual specifications"""

    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        """The all function includes all the values that are satisfied
        inside of its logic, and the map function uses a lambda to go through
        every single element and apply a lambda to it.

        Lambda takes a specification and checks if it is satisfied for this particular
        item (we have many items stored in args), and we go through self.args

        So we go through every single argument checking whether it is satisfied or not,
        which is handled by the map function, and then we use all() which checks that
        every single argument is a boolean value of True."""

        return all(map(lambda spec: spec.is_satisfied(item), self.args))


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # Old approach:
    pf = ProductFilter()
    print("Green products (old):")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f" - {p.name} is green")

    # New approach:
    bf = BetterFilter()

    print("Green products (new):")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f" - {p.name} is green")

    print("Large products:")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name} is large")

    # Combinator

    print("Large blue items:")
    # large_blue = AndSpecification(large,
    #   ColorSpecification(Color.BLUE))
    large_blue = large & ColorSpecification(Color.BLUE)  # Works thanks to __and__ method
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is large and blue")
