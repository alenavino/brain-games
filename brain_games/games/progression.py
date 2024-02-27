from random import randint


def progression():
    exercise = 'What number is missing in the progression?'
    first_number = randint(1, 100)
    difference = randint(1, 100)
    lst = [first_number]
    while len(lst) < 10:
        last_number = lst[-1]
        lst.append(last_number + difference)
    secret = randint(1, 10)
    correct_answer = lst[secret]
    lst[secret] = '..'
    expression = ''
    for element in lst:
        expression += str(element)
        expression += ' '
    return exercise, expression, correct_answer
