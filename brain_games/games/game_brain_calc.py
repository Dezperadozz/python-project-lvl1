from random import randint
from random import choice

from brain_games.cli import welcome_user
from brain_games.games.game_engine import show_wrong_answer_info, get_player_name, show_confirmation
from brain_games.games.game_engine import congratulate_player
from brain_games.games.game_engine import greet
from brain_games.games.game_engine import input_answer
from brain_games.games.game_engine import ROUNDS

SIGNS = ['+', '-', '*']


def show_rules():
    print('What is the result of the expression?')


def calc_expression(random_num1, random_num2, random_sign):
    if random_sign == '+':
        return random_num1 + random_num2
    elif random_sign == '-':
        return random_num1 - random_num2
    else:
        return random_num1 * random_num2


def show_question(random_num1, random_num2, random_sign):
    print(f'Question: {random_num1} {random_sign} {random_num2}')


def make_answers():
    count_answers = 0
    player_name = get_player_name()
    while count_answers < ROUNDS:
        random_num1 = randint(0, 100)
        random_num2 = randint(0, 100)
        random_sign = choice(SIGNS)
        show_question(random_num1, random_num2, random_sign)
        answer = input_answer()
        correct_answer = calc_expression(random_num1, random_num2, random_sign)
        if correct_answer == answer:
            count_answers += 1
            show_confirmation()
        else:
            show_wrong_answer_info(answer, correct_answer, player_name)
            break
        if count_answers == ROUNDS:
            congratulate_player(player_name)


def start_game():
    greet()
    show_rules()
    welcome_user()
    make_answers()
