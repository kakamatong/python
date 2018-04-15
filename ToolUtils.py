import threading

class ToolUtils(object):
    def __init__(self):
        pass
    @staticmethod
    def timerForever(t, func):
        def myFunc():
            func()
            time = threading.Timer(t, myFunc)
            time.start()
        time = threading.Timer(t, myFunc)
        time.start()

    @staticmethod
    def timer(t, func):
        time = threading.Timer(t, func)
        time.start()
    pass