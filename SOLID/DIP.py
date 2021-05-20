#Dependency Inversion Principle (DIP)

#high levels classes should not depend on low leve modules,
#instead they should depend on abstraction.

from enum import Enum
from abc import abstractmethod

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass

#Low level module
class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )
    
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

#how to break the DIP -->
#High level module
class Research:
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}')

    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

Relationships = Relationships()
Relationships.add_parent_and_child(parent, child1)
Relationships.add_parent_and_child(parent, child2)

Research(Relationships)

#What was the problem, and how we fixed it -->

'''

So relations in line 44 is the way the Relationships module in line 23
stores relations, which is a list.

Now, imagine we decide to change from a list to something else (e.g. a dictionary).
Because you are accessing the internal mechanism (i.e. relationship = list), in your
high level module, so you can't change line 25, or else all between lines
44-47 will break.
We really want to avoid this.

To solve this, Research should not depend on a concrete implementation (i.e. Relationships),
but rather on some sort of abstraction that can subsequently change.
That is why we build the "RelationshipBrowser", containing an abstract method.
Now, we move the whole functionality in lines 44-47 to a low level module.

WHY is this better?
it is better because if you need to change relationships = list into a dictionary or something
else, you would ony need to adapt the lines 35-38, and ALL the high level modules will work.

Research(Relationships) in line 62 inherits RelationshipBrowser, and has its methods enherited.


'''