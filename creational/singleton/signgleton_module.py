i = -1
registry = {}


def add(obj):
    global i
    i += 1
    registry[i] = obj
