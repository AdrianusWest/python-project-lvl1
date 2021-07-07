import prompt
from brain_games.cli import welcome


def congratulations(name):
    print(f'Congratulations, {name}!')


def show_error(user_answer, correct_answer, name):
    print(
        f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.'
    )
    print(f"Let\'s try again, {name}!")


def greet(name):
    print(f'Hello, {name}!')


def engine(game):
    welcome()
    print(game.INSTRUCTION)
    name = prompt.string('May I have your name? ')
    greet(name)
    rounds = 3
    while rounds:
        (question, correct_answer) = game.generate_question()
        user_answer = prompt.string(f'{question} ')
        if user_answer == correct_answer:
            print('Correct!')
            rounds -= 1
        else:
            show_error(user_answer, correct_answer, name)
            exit()

    congratulations(name)
