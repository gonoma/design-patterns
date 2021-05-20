from abc import ABC
from collections.abc import Iterable 

class Operations(ABC, Iterable):
    @property
    def sum(self):
        result = 0
        for x in self:
            #print(x)
            if isinstance(x, SingleValue):
                x = x.value
            elif isinstance(x, ManyValues):
                y = 0
                for value in x:
                    y += value
                x = y
            result += x
        return result


class SingleValue(Operations):
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        yield self


class ManyValues(list, Operations):
    def __init__(self):
        super().__init__()


single_value = SingleValue(11)
other_values = ManyValues()
other_values.append(22)
other_values.append(33)
# make a list of all values
all_values = ManyValues()
all_values.append(single_value)
all_values.append(other_values)

print(all_values.sum)
