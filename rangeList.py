
#This file should be compiled for performance

class rangeList:
    values = 0

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
        pass


raw1 = "2-4-5-12-53"
raw2 = "1-4-13-33-44-51"
list1 = rangeList(raw=raw1)
list2 = rangeList(raw=raw2)
print(list1)
print(list2)