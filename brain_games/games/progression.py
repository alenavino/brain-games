from random import randint


def progression():
    exercise = 'What number is missing in the progression?'
    first_number = randint(1, 100)
    difference = randint(1, 100)
    list = [first_number]
    while len(list) < 10:
        last_number = list[-1]
        list.append(last_number + difference)
    secret = randint(1, 10)
    correct_answer = list[secret]
    list[secret] = '..'
    expression = ''
    for element in list:
        expression += str(element)
        expression += ' '
    return exercise, expression, correct_answer
    