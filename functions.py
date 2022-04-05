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
        self.hour = (self.timenum - (self.timenum % 60)) / 60
        self.minute = self.timenum % 60

    def setTime(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.updateNum()

    def setNum(self, timeNum):
        self.timenum = timeNum
        self.updateTime()


class rangeList:
    stamps = [] #Place numbers inside
    def __and__(self, other):
        pass

