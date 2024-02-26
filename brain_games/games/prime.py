from random import randint


def prime():
    exercise = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    number = randint(1, 100)
    denominator = number - 1
    correct_answer = 'yes'
    while denominator > 1:
        if number % denominator == 0:
            correct_answer = 'no'
            break
        else:
            denominator -= 1
    return exercise, number, correct_answer
