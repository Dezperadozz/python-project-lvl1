import prompt
from random import randint

from brain_games.cli import welcome_user
from brain_games.cli import get_name

ANSWERS = ['yes', 'no']


def check_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def wrong_answer_info(answer, correct_answer, player_name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {player_name}!")


def make_answers():
    answers_for_win = 3
    count_answers = 0
    player_name = get_name()
    while count_answers < answers_for_win:
        random_num = randint(0, 100)
        print(f'Question: {random_num}')
        answer = prompt.string('Your answer : ')
        correct_answer = check_even(random_num)
        if answer.lower() not in ANSWERS:
            wrong_answer_info(answer, correct_answer, player_name)
            break
        if answer.lower() == correct_answer:
            count_answers += 1
            print('Correct!')
        else:
            wrong_answer_info(answer, correct_answer, player_name)
            break
    if count_answers == answers_for_win:
        print(f'Congratulations, {player_name}!')


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    welcome_user()
    make_answers()


if __name__ == "__main__":
    main()
