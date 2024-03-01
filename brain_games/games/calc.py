from random import randint, choice


def calc():
    exercise = 'What is the result of the expression?'
    first_number = randint(0, 100)
    operation = choice(['+', '-', '*'])
    second_number = randint(0, 100)
    expression = f'{first_number} {operation} {second_number}'
    correct_answer = eval(expression)
    return exercise, expression, correct_answer
