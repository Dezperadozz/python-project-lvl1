import math
from random import randint

from brain_games.cli import welcome_user
from brain_games.games.game_engine import show_wrong_answer_info, get_player_name, show_confirmation
from brain_games.games.game_engine import congratulate_player
from brain_games.games.game_engine import greet
from brain_games.games.game_engine import input_answer
from brain_games.games.game_engine import ROUNDS


def show_rules():
    print('Find the greatest common divisor of given numbers.')


def show_question(random_num1, random_num2):
    print(f'Question: {random_num1} {random_num2}')


def make_answers():
    count_answers = 0
    player_name = get_player_name()
    while count_answers < ROUNDS:
        random_num1 = randint(0, 100)
        random_num2 = randint(0, 100)
        show_question(random_num1, random_num2)
        answer = input_answer()
        correct_answer = math.gcd(random_num1, random_num2)
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
