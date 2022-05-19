
#This file should be compiled for performance reasons

class rangeList:
    values = []

    """def read(self, raw):
        self.values = raw.split('-')
        for i in range(len(self.values)):
            self.values[i] = int(self.values[i])"""

    def __init__(self, raw):
        self.values = raw.split('-')
        for i in range(len(self.values)):
            self.values[i] = int(self.values[i])

    def __repr__(self):
        state = False
        value = ""
        for i in range(len(self.values)):
            state = not state
            value += f"{self.values[i]} -{'T' if state else 'F'}- "

        return value

    def __and__(self, other):
        result = rangeList
        stamp = 0
        state = False
        stateA = False
        stateB = False
        i = 0
        j = 0



raw1 = "2-4-5-12-53"
raw2 = "1-4-13-33-44-51"
list1 = rangeList(raw=raw1)
list2 = rangeList(raw=raw2)
anded = list1 & list2
print("  1: ", list1)
print("  2: ", list2)
print("AND: ", anded)