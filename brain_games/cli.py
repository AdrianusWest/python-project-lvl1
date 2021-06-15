import prompt

"Запрос имени пользователя"

def welcome_user():
    return prompt.string('May I have your name? ', empty=False)
