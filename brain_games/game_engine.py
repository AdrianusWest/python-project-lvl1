import prompt


def show_error(user_answer, correct_answer, name):
    print(
        f'{user_answer} is wrong answer ;(. '
        f'Correct answer was {correct_answer}.'
    )
    print(f"Let\'s try again, {name}!")


def engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.INSTRUCTION)

    number_of_rounds = 3

    while number_of_rounds:
        question, correct_answer = game.get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer != correct_answer:
            show_error(user_answer, correct_answer, name)
            exit()

        print('Correct!')
        number_of_rounds -= 1

    print(f'Congratulations, {name}!')
