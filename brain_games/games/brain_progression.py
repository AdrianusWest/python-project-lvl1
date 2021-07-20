import random

INSTRUCTION = 'What number is missing in the progression?'


def get_question_and_answer():
    step = random.randint(1, 10)
    start_number = random.randint(1, 1000)
    progression_length_count = 11

    progression = list(
        range(start_number,
              (start_number + progression_length_count * step),
              step))

    random_index = random.randrange(0, progression_length_count)
    answer, progression[random_index] = progression[random_index], '..'
    question = ' '.join(map(str, progression))
    return question, str(answer)
