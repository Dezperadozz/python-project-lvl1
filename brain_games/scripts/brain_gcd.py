import prompt
import math
from random import randint

from brain_games.cli import welcome_user
from brain_games.cli import get_name


def wrong_answer_info(answer, correct_answer, player_name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {player_name}!")


def make_answers():
    answers_for_win = 3
    count_answers = 0
    player_name = get_name()
    while count_answers < answers_for_win:
        random_num1 = randint(0, 100)
        random_num2 = randint(0, 100)
        print(f'Question: {random_num1} {random_num2}')
        answer = prompt.integer('Your answer : ')
        correct_answer = math.gcd(random_num1, random_num2)
        if correct_answer == answer:
            count_answers += 1
            print('Correct!')
        else:
            wrong_answer_info(answer, correct_answer, player_name)
            break
        if count_answers == answers_for_win:
            print(f'Congratulations, {player_name}!')


def main():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.')
    welcome_user()
    make_answers()


if __name__ == "__main__":
    main()