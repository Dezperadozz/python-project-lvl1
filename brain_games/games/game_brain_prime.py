import math
from random import randint

from brain_games.cli import welcome_user
from brain_games.games.game_engine import show_wrong_answer_info, get_player_name, show_confirmation
from brain_games.games.game_engine import congratulate_player
from brain_games.games.game_engine import greet
from brain_games.games.game_engine import input_answer
from brain_games.games.game_engine import ROUNDS


def show_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def show_question(random_num):
    print(f'Question: {random_num}')


def check_prime(num):
    if num == 1:
        return 'yes'
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return 'no'
        return 'yes'


def make_answers():
    count_answers = 0
    player_name = get_player_name()
    while count_answers < ROUNDS:
        random_num = randint(1, 100)
        show_question(random_num)
        answer = input_answer()
        correct_answer = check_prime(random_num)
        if answer.lower() == correct_answer:
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
