from random import randint

from brain_games.cli import welcome_user
from brain_games.games.game_engine import show_wrong_answer_info, get_player_name, show_confirmation
from brain_games.games.game_engine import congratulate_player
from brain_games.games.game_engine import greet
from brain_games.games.game_engine import input_answer
from brain_games.games.game_engine import ROUNDS

PROGRESSION_LEN = 10


def show_rules():
    print('What number is missing in the progression?')


def show_question():
    print('Question:', end=' ')


def generate_progression():
    progression_first_element = randint(1, 10)
    progression_step = randint(1, 10)
    progression = [0] * PROGRESSION_LEN
    progression[0] = progression_first_element
    for i in range(1, PROGRESSION_LEN):
        progression[i] = progression[i - 1] + progression_step
    return progression


def show_progression(progression, progression_hidden_element):
    for i in range(0, PROGRESSION_LEN):
        if i == progression_hidden_element:
            print('..', end=' ')
        else:
            print(progression[i], end=' ')
    print()


def make_answers():
    count_answers = 0
    player_name = get_player_name()
    while count_answers < ROUNDS:
        progression = generate_progression()
        progression_hidden_element = randint(0, PROGRESSION_LEN - 1)
        show_question()
        show_progression(progression, progression_hidden_element)
        answer = input_answer()
        if answer == progression[progression_hidden_element]:
            count_answers += 1
            show_confirmation()
        else:
            show_wrong_answer_info(answer, progression[progression_hidden_element], player_name)
        if count_answers == ROUNDS:
            congratulate_player(player_name)


def start_game():
    greet()
    show_rules()
    welcome_user()
    make_answers()
