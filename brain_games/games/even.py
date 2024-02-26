from random import randint


def even():
    exercise = 'Answer "yes" if the number is even, \
otherwise answer "no".'
    number = randint(1, 100)
    correct_answer = ''
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return exercise, number, correct_answer
