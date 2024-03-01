from random import randint


def is_even(num):
    return num % 2 == 0


def even():
    exercise = 'Answer "yes" if the number is even, \
otherwise answer "no".'
    number = randint(1, 100)
    correct_answer = ''
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return exercise, number, correct_answer
