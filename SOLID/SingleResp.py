# Single Responsibility Principle (SRP)
# Separation Of Concerns (SOC)


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # WHAT IS __STR__ ?  :

    # without __str__
    """
    In [1]:         class Person:
   ...:             pass
   ...: 
    In [2]:         p = Person()
    In [3]:         print p
    <__main__.Person instance at 0x7faffb3ac5f0>
    """
    # with __str__
    """
    In [4]:         class Person:
    ...:     def __str__(self):
    ...:         return 'Person class'
    ...:     
    In [5]: p = Person()
    In [6]: print p
    Person class
    
    """

    # Break the SRP by adding additional responsibility
    # that never really asked for.

    """The problem with this is that we added a
    second responsibility of "persistence" to the journal class.

    It may seem like a good idea, but if you think about
    a complete application in which in addition to Journals
    you have other types of classes (e.g. Novel, Exercise book, etc)
    all these types may have their own save, load and load from web methods,
    and this functionality might have to be centrally changed at some point.
    For example, by saving a file you may want to add additional functionality
    to make sure you are allowed to write into a particular directory.

    So if you adopt this approach, you will have to go into every single class
    in your application and change their save method, or their load.

    So you want to take the responsibility of persistence, and move it to a 
    separate class.
    

    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def low_from_web(self, uri):
        pass
    """


class PersistenceManager:
    # we don't use self, we make it static.
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}")

file = r"C:\Users\gonza\OneDrive\Documentos\MA_Shit\Udemy\journal.txt"
PersistenceManager.save_to_file(j, file)
"""the r in line 90 is a "raw string" and is used to make sure python does not
understand \name.txt and a new like ame.txt, but rather like a file name.txt """

# fh = file handler
with open(file) as fh:
    print(fh.read())

# In the output everything is printed twice, the first time is when
# we printed them using str, and the second one is when we serialised
# them into a file and then reading them from that file.

# A god object would be a file of class that has everything inside it,
# this is not good, a god obect should be splitted and subdivided into
# adequate design patterns.
