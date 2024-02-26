from random import randint


def gcd():
    exercise = 'Find the greatest common divisor of given numbers.'
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    expression = f'{first_number} {second_number}'
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    correct_answer = first_number + second_number
    return exercise, expression, correct_answer
