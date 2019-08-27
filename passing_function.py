def method_caption(another):
    return another()


def add_two_numbers():
    return 30 + 77


# print(methodcaption(add_two_numbers))

# print(methodcaption(lambda: 30 + 100))

my_list = [21, 45, 60, 24]
print(list(filter(lambda x: x % 2 == 0, my_list)))

(lambda x: x * 3)(5)


def f(x):
    return x * 3
