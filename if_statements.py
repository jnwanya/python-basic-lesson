# names = ['John', 'Smith', 'Obi', 'Mikel']
# name = input('Enter name of student: ')
""" if name in names:
    print('Name {} is in list'.format(name))
else:
    print('Name {} not on list'.format(name))
"""
# if name not in names:
#    print('Name not on the list')

# known_names = []


def who_do_you_know():
    user_input = input('Enter names you know separated by comma: ')
    people = [name.strip() for name in user_input.split(',')]
    return people


def ask_user():
    input_name = input('Enter a name: ')
    if input_name in who_do_you_know():
        print('{} is a known name'.format(input_name))
    else:
        print('{} is not a known name'.format(input_name))


# known_names = who_do_you_know()
# print(known_names)
ask_user()
