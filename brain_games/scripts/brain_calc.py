#!/usr/bin/env python3


from random import randint, choice
import prompt


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def calc():
    user_name = welcome_user()
    print('What is the result of the expression?')
    i = 1
    while i < 4:
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
        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            break
        i += 1
        if i > 3:
            print(f'Congratulations, {user_name}!')


def main():
    greet()
    calc()


if __name__ == '__main__':
    main()
