#!/usr/bin/env python3
from brain_games.game_engine import engine
from brain_games.games import brain_even


"""скрипт запуска игры"""
def main():
    engine(brain_even)


if __name__ == '__main__':
    main()
