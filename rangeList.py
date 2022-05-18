
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
        print("got to the function")
        result = rangeList
        stamp = 0
        state = False
        stateA = False
        stateB = False
        while bool(self.values) and bool(other.values):
            print(self, other)
            if self.values[0] > other.values:
                stateA = not stateA
                stamp = self.values.pop(0)
            else:
                stateB = not stateB
                stamp = other.values.pop(0)

            if (stateA and stateB) != state:
                state = not state
                result.values.append(stamp)

        return result



raw1 = "2-4-5-12-53"
raw2 = "1-4-13-33-44-51"
list1 = rangeList(raw=raw1)
list2 = rangeList(raw=raw2)
print("  1: ", list1)
print("  2: ", list2)
print("AND: ", list1 and list2)