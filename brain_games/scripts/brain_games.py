from brain_games.cli import welcome_user


"""Приветствие"""


def main():
    print('Welcome to the Brain Games!')
    welcome = welcome_user()
    print('Hello,' + welcome + '!')


if __name__ == '__main__':
    main()
