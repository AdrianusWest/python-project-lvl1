import random

INSTRUCTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(num):
    return num % 2


def get_question_and_answer():
    num = random.randint(1, 100)
    question = f'{num}'
    correct_answer = 'no' if is_even(num) else 'yes'
    return question, correct_answer
