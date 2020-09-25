import prompt
from random import randint
from random import choice

from brain_games.cli import welcome_user
from brain_games.cli import get_name

SIGNS = ['+', '-', '*']


def calc_expression(random_num1, random_num2, random_sign):
    if random_sign == '+':
        return random_num1 + random_num2
    elif random_sign == '-':
        return random_num1 - random_num2
    else:
        return random_num1 * random_num2


def wrong_answer_info(answer, correct_answer, player_name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {player_name}!")


def make_answer():
    answers_for_win = 3
    count_answers = 0
    player_name = get_name()
    while count_answers < answers_for_win:
        random_num1 = randint(0, 100)
        random_num2 = randint(0, 100)
        random_sign = choice(SIGNS)
        print(f'Question: {random_num1} {random_sign} {random_num2}')
        answer = prompt.integer('Your answer : ')
        correct_answer = calc_expression(random_num1, random_num2, random_sign)
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
    print('What is the result of the expression?')
    welcome_user()
    make_answer()


if __name__ == "__main__":
    main()
