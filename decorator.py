import functools

'''
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print('In the decorator')
        func()
        print('After the decorator')
    return function_that_runs_func


@my_decorator
def addition():
    print('I am the function')
'''


def decorator_with_argument(number):
    def my_new_docorator(func):
        @functools.wraps(func)
        def function_that_runs_with_arg(*args, **kwargs):
            print('In the decorator: {}'.format(number))
            if number == 100:
                print('Not running the function')
            else:
                func(*args, **kwargs)
            print('After the decorator')
        return function_that_runs_with_arg
    return my_new_docorator


@decorator_with_argument(10)
def my_addition(x, y):
    print('my_addition function is running')
    # return x + y


my_addition(50, 70)
