# Interface Segregation Principle

# The idea is that you don't want to stick
# too many elements (e.g. methods) into an interface.

from abc import abstractmethod

# Machine for printing and scanning example:


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultifunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


# this one cannot fax, cannot scan.
class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok
        pass

    def fax(self, document):
        pass  # First approach: do nothing. This is not good, can confuse people.

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError("Printer cannot scan!")  # Second approach, raise error. This is better...
                                                           # But still not good enough, it could crash your entire app
                                                           # Simply because down the line you may need it,
                                                           # and all it does is give back errors


# Now, the idea of ISP, is that instead of having one large interface (i.e. Machine in this case),
# you want to keep things granular, you want to split the Machine interface into separate parts
# that people can implement (i.e. interfaces Printer, Scanner, FaxMachine)


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


# In case you really want to have the single interface at the beginning, you can do it correctly like so:


class MultifunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

# And implemented like this:


class MultifunctionMachine(MultifunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
