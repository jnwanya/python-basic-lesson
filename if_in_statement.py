import random
number = random.randint(1, 21)
user_input = input("Enter 'y' if you want to play a game? ")

if user_input in ('y', "Y"):
    user_guess = int(input('Guess our number: '))
    if user_guess == number:
        print('You made the right guess')
    elif user_guess - number in (-1, 1):
        print(f'Your guess was off by one. Our number: {number}')
    else:
        print(f'Your guess wrong. Our number: {number}')
