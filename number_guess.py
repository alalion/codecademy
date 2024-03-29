"""
It is Number Guess game that rolls a pair of dice and asks the user to guess the sum. If the users guess is equal to the total value of the dice roll, the user wins!
"""
from random import randint
from time import sleep


def get_user_guess():
    guess = int(input('Guess a number: '))
    return guess


def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print('The maximum possible value is %d') % max_val
    guess = get_user_guess()
    if guess > max_val:
        print('Your guess is invalid: it is higher than maximum value')
    else:
        print('Rolling...')
        sleep(2)
        print('First roll: %d') % first_roll
        sleep(1)
        print('Second roll: %d') % second_roll
        total_roll = first_roll + second_roll
        print(total_roll)
        print('Result...')
        sleep(1)
    if guess == total_roll:
        print('You won!')
    else:
        print('You lost everything!')


roll_dice(6)
