import math
import random

INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    divisor = 2
    while divisor <= math.sqrt(num):
        if num % divisor:
            divisor += 1
        else:
            return True
    return False


def get_question_and_answer():
    num = random.randint(1, 100)
    question = f'{num}'
    correct_answer = 'no' if is_prime(num) else 'yes'
    return question, correct_answer
