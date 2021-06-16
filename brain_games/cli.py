import prompt


"""Запрос имени пользователя:

def welcome_user() -> str:
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name

"""


def welcome_user():
    return prompt.string('May I have your name? ', empty=False)
