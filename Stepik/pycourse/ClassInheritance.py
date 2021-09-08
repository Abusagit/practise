import time


class Loggable:
    def __init__(self):
        pass

    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, args):
        super().append(args)
        return super().log(args)


logggg = LoggableList([1, 2, 3, 4])
logggg.append([1, 2, 3, 4, 5])