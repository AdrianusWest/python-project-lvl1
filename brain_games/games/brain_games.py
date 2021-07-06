from brain_games.cli import welcome, greet
import prompt


def demo():
    welcome()
    name = prompt.string('May I have your name? ')
    greet(name)
