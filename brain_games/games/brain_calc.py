import operator
import random

INSTRUCTION = 'What is the result of the expression?'


def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    random_operator = random.choice(list(operators.keys()))

    question = f'{num1} {random_operator} {num2}'
    correct_answer = str(operators[random_operator](num1, num2))
    return question, correct_answer
