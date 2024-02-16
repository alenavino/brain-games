#!/usr/bin/env python3


from random import randint
import prompt


name_user = ''


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    global name_user
    name_user = name


def even():
    i = 1
    while i < 4:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        number = randint(1, 100)
        correct_answer = ''
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name_user}!")
            break
        i += 1
        if i > 3:
            print(f'Congratulations, {name_user}!')


def main():
    greet()
    welcome_user()
    even()


if __name__ == '__main__':
    main()