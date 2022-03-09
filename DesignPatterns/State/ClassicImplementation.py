"""
A Light Switch

You are essentially alternating from one class to the other depending on the On or Off states.
If the switch is on, then switch.state class is equal to OnState()
If the switch is off, then switch.state class is equal to OffState()
by default the switch is off.
"""
from abc import ABC


class Switch:
    def __init__(self):
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


class State(ABC):
    def on(self, switch):
        print("Light is already on")

    def off(self, switch):
        print("Light is already off")


class OnState(State):
    def __init__(self):
        print("Light turned on")

    def off(self, switch):
        print("Turning Light off...")
        switch.state = OffState()


class OffState(State):
    def __init__(self):
        print("Light turned Off")

    def on(self, switch):
        print("Turning light on...")
        switch.state = OnState()


if __name__ == "__main__":
    sw = Switch()

    sw.on()

    sw.off()

    sw.off()
