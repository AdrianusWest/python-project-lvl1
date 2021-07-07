import prompt
from brain_games.cli import welcome
from brain_games.game_engine import greet


def demo():
    welcome()
    name = prompt.string('May I have your name? ')
    greet(name)
