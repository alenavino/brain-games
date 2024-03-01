from brain_games.cli import welcome_user
import prompt


def engine(game):
    user_name = welcome_user()
    i = 1
    while i < 4:
        exercise, expression, correct_answer = game()
        if i == 1:
            print(exercise)
        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            break
        if i == 3:
            print(f'Congratulations, {user_name}!')
        i += 1
