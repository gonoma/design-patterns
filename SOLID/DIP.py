# Dependency Inversion Principle (DIP)

# High level classes should not depend on concretions,
# instead, they should depend on abstractions.

from enum import Enum
from abc import abstractmethod


class Relationship(Enum):
    """Identifiers, e.g. 0 = Parent"""

    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


# Low level module
class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# how to break the DIP --> commented out code
# High level module
class Research:
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}')

    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}")


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

Relationships = Relationships()
Relationships.add_parent_and_child(parent, child1)
Relationships.add_parent_and_child(parent, child2)

Research(Relationships)

# What was the problem, and how we fixed it -->

"""

So relations in line 48 is the way the Relationships module in line 32
stores relations, which is a list.

Now, imagine we decide to change relations attribute from a list to something else (e.g. a dictionary).
Because you are accessing the internal storage mechanism Relationships.relations of your low level module, in your
high level module, if you change relations to a dict it will break all your code that is using it (this could be a lot of code),
because it depends on it being a list.

We really want to avoid this.

To solve this, Research should not depend on a concrete implementation (i.e. __init__() commented out code),
but rather on some sort of abstraction that can subsequently change.
That is why we build the "RelationshipBrowser", containing an abstract method.
Now, we move the whole functionality to a low level module Relationships.find_all_children_of().

WHY is this better?
it is better because if you need to change relationships = list into a dictionary or something
else, you would only need to adapt the lines in Relationships.find_all_children_of(), 
and ALL the high level modules will work.

"""
