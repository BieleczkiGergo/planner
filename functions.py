class timestamp:
    hour = 0
    minute = 0
    timenum = 0

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.timenum = self.hour*60 + self.minute

    def updateNum(self):
        self.timenum = self.hour*60 + self.minute

    def updateTime(self):
        self.hour = self.timenum % 60
        self.minute = self.timenum - (self.hour*60)


class activity:
    events = []


def rangeAND(range1, range2):
    state1 = False
    state2 = False
    stateU = False
    rangeU = activity()
    going = True
    ct = 0
    while going:
        if bool(range1):
            if bool(range2):
                if range1.events[0] < range2.events[0]:
                    ct = range1.events.pop(0)
                    state1 = not state1

                elif range2.events[0] < range1.events[0]:
                    ct = range2.events.pop(0)
                    state2 = not state2

                else:
                    pass

        if stateU != state1 and state2:
            stateU = not stateU
            rangeU.events.append(ct)


    return rangeU


act1 = activity
act1.events = [timestamp(0, 20), timestamp(1, 10), timestamp(2, 40), timestamp(2, 52)]
act2 = activity
act2.events = [timestamp(0, 30), timestamp(1, 20), timestamp(2, 20), timestamp(2, 45)]

available = rangeAND(act1, act2)
for i in available.events:
    print(f"Timestamp at hour: {i.hour}, minute: {i.minute}")