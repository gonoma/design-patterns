class Event(list):
    """List of functions that need to be called/invoked whenever this Event happens"""

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = (
            Event()
        )  # Now a Doctor class can subscribe to this Event and get notifications.

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f"{name} needs a doctor at {address}")


if __name__ == "__main__":
    person = Person("Sherlock", "221B Baker St")

    person.falls_ill.append(lambda name, address: print(f"{name} is ill"))

    person.falls_ill.append(call_doctor)  # Simple code

    # Whenever the person catches a cold, the functions to call a doctor are triggered
    person.catch_a_cold()

    print("\n")
    # Now Sherlock recovers
    person.falls_ill.remove(call_doctor)

    # Remove the lambda function as well
    is_ill = person.falls_ill[0]
    person.falls_ill.remove(is_ill)

    # The catch a cold method no longer calls a doctor, because the person is healthy
    person.catch_a_cold()

"""
Overall very succinct way of defining Events using only a list of functions that are callable.
And you can set it up in the initializer (Person) and then inform a client using the API if the person is ill or not.
Using append for subscription and remove for unsubscription of a doctor service.
"""
