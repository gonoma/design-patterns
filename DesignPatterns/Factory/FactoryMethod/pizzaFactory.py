from __future__ import annotations
from abc import ABC, abstractmethod


class PizzaCreator(ABC):
    """
    The PizzaCreator class declares the factory method (_bake) that is supposed to return an
    object of a PizzaProduct class. The PizzaCreator's subclasses should provide the
    implementation of this _bake method, PizzaCreator simply defines the interface.
    """

    # Factory Method
    # Because it's an abstract method, it's "compulsory" for the child class to define it
    # Think about it like a "compulsory interface" that the child class has to overwrite.
    # In this case, to bake one pizza or another...
    @abstractmethod
    def _bake(self):
        """
        Bake the pizza.
        """
        pass

    def create_pizza(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        pizza = self._bake()

        # Now, use the product.
        result = f"PizzaCreator: The same PizzaCreator's code has just worked with {pizza.eat_pizza()}"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class PizzaMargheritaCreator(PizzaCreator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def _bake(self) -> Pizza:
        return PizzaMargherita(base='tomato', cheese='mozzarella', herb='basil')


class PizzaMarinaraCreator(PizzaCreator):
    def _bake(self) -> Pizza:
        return PizzaMarinara(base='tomato', herb='oregano')


class Pizza(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    def __init__(self,
                 base: str,
                 cheese: str = None,
                 herb: str = None):
        self.base = base
        self.cheese = cheese
        self.herb = herb

    @abstractmethod
    def eat_pizza(self) -> str:
        pass

"""
Concrete Products provide various implementations of the Product interface.
"""

class PizzaMargherita(Pizza):
    def eat_pizza(self) -> str:
        return "{Result of the PizzaMargherita}"


class PizzaMarinara(Pizza):
    def eat_pizza(self) -> str:
        return "{Result of the PizzaMarinara}"


def client_code(creator: PizzaCreator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the PizzaCreator's class, but it still works.\n"
          f"{creator.create_pizza()}", end="")


if __name__ == "__main__":
    print("App: Launched with the PizzaMargherita.")
    client_code(PizzaMargheritaCreator())
    print("\n")

    print("App: Launched with the PizzaMarinara.")
    client_code(PizzaMarinaraCreator())
