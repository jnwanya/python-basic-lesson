add = lambda x, y: x + y
print(add(4, 5))


def double(x):
    return x * 2


sequence = [2, 4, 5, 6]
# doubled = [double(x) for x in sequence]
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)
