def add(*args):
    x, y = args
    return x + y


def subtract(*args):
    x, y = args
    return x - y


mapper = {
    "plus": add,
    "minus": subtract
}


data = {
    'plus': [5, 3],
    'minus': [3, 4],
}

for key, val in data.items():

    print(mapper[key](*val))


