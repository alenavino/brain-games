from random import randint, choice


def calc():
    exercise = 'What is the result of the expression?'
    first_number = randint(0, 100)
    operation = choice(['+', '-', '*'])
    second_number = randint(0, 100)
    expression = f'{first_number} {operation} {second_number}'
    correct_answer = 0
    if operation == '+':
        correct_answer = first_number + second_number
    elif operation == '-':
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    return exercise, expression, correct_answer
