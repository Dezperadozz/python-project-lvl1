import prompt
import math
from random import randint

from brain_games.cli import welcome_user
from brain_games.cli import get_name


def check_prime(num):
    if num == 1:
        return 'yes'
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return 'no'
        return 'yes'


def wrong_answer_info(answer, correct_answer, player_name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {player_name}!")


def make_answer():
    player_name = get_name()
    random_num = randint(1, 100)
    print(f'Question: {random_num}')
    answer = prompt.string('Your answer : ')
    if answer.lower() == check_prime(random_num):
        print('Correct!')
        print(f'Congratulations, {player_name}!')
    else:
        wrong_answer_info(answer, check_prime(random_num), player_name)


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    welcome_user()
    make_answer()


if __name__ == "__main__":
    main()
