
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
        result = []
        stamp = 0
        temp = False
        state = False
        stateA = False
        stateB = False
        while bool(self.values) and bool(other.values):
            if self.values[0] < other.values[0]:
                stamp = self.values.pop(0)
                stateA = not stateA
            else:
                stamp = other.values.pop(0)
                stateB = not stateB
            temp = stateA and stateB
            if temp != state:
                result.append(stamp)

        return result



raw1 = "2-4-5-12-53"
raw2 = "1-4-13-33-44-51"
list1 = rangeList(raw=raw1)
list2 = rangeList(raw=raw2)
print(list1)
print(list2)
print(list1 and list2)