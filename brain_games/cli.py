import prompt

from brain_games.games.game_engine import add_player


def welcome_user():
    name = prompt.string('May I have your name? ')
    add_player(name)
    print(f'Hello, {name}!')
