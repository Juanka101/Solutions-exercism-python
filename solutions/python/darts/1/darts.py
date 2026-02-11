def score(x, y):
    x = x ** 2
    y = y ** 2
    radio = 100

    if (x + y) <= radio:
        if (x + y) <= radio * 0.01:
            return 10
        elif (x + y) <= radio * 0.25:
            return 5
        else:
            return 1
    else:
        return 0
        