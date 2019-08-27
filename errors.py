def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('You cannot divide by zero')
    return dividend / divisor


grades = [12, 45]
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print('There are no grade yet')
except ValueError as e:
    print('There is an Value Error')
else:
    print(f"Average grade is {average}")
finally:
    print('Finally ended.')
