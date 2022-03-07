"""
Problems with this design Pattern
e.g. What happens when you have a property that is dependent on another property ?
So when the "can_vote" depends on age property for example.
The lines with "###" comments are the solution to the problem.
This solution is not scalable, and it is very hard to scale this problem
in an application where hundreds of properties depend on each other, like in excel cells.
"""


class Event(list):
    """List of functions that need to be called/invoked whenever this Event happens"""

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def can_vote(self):
        return self._age >= 18

    # Getter
    @property
    def age(self):
        print("GETTER")
        return self._age

    @age.setter
    def age(self, value):
        print("SETTER")
        if self._age == value:
            return

        old_can_vote = self.can_vote  ###

        self._age = value
        self.property_changed("age", value)

        if old_can_vote != self.can_vote:  ###
            self.property_changed("can_vote", self.can_vote)  ###


if __name__ == "__main__":
    # Handler
    def person_changed(name, value):
        if name == "can_vote":
            print(f"Voting ability changed to {value}")

    p = Person()
    p.property_changed.append(person_changed)

    for age in range(16, 21):
        print(f"Changing age to {age}")
        p.age = age  # Sets data
        print(p.age)  # Gets data
