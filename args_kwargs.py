def my_method(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


def long_arg_method(*args):
    return sum(args)


def kwargs_method(*args, **kwargs):
    print(args)
    print(kwargs)


kwargs_method(1, 2, 45, name='John', location='UK')
