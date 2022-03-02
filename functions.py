class timestamp:
    hour = 0
    minute = 0
    timenum = 0

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.timenum = self.hour*60 + self.minute

    def update(self):
        self.timenum = self.hour*60 + self.minute



class activity:
    events = []



def rangeAND(range1, range2):
    state1 = False
    state2 = False
    i1 = 0
    i2 = 0
    stateU = False
    rangeU = activity()
    while(bool(range1) and bool(range2)):
        if range1.events[i1].timenum < range2.events[i2].timenum:
            state1 = not(state1)
            stateU = state1 and state2
            state1.events.pop(0)
            if stateU:
                rangeU.events.append(range1.events[i1].timenum)

        elif range1.events[i1].timenum > range2.events[i2].timenum:
            state2 = not(state2)
            stateU = state1 and state2
            state2.events.pop(0)
            if stateU:
                rangeU.events.append(range2.events[i2].timenum)

        else:
            state1 = not(state1)
            state2 = not(state2)
            stateU = state1 and state2
            state1.events.pop(0)
            state2.events.pop(0)
            if stateU:
                rangeU.events.append(range1.events[i1].timenum)

        return rangeU