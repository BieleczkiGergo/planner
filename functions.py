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
    while going:
        if bool(range1):
            pass

    return rangeU


act1 = activity
act1.events = [timestamp(0, 20), timestamp(1, 10), timestamp(2, 40), timestamp(2, 52)]
act2 = activity
act2.events = [timestamp(0, 30), timestamp(1, 20), timestamp(2, 20), timestamp(2, 45)]

available = rangeAND(act1, act2)
for i in available.events:
    print(f"Timestamp at hour: {i.hour}, minute: {i.minute}")