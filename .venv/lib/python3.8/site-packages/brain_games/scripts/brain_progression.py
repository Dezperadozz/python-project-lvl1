import prompt
from random import randint

from brain_games.cli import welcome_user
from brain_games.cli import get_name

PROGRESSION_LEN = 10


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


def wrong_answer_info(answer, correct_answer, player_name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {player_name}!")


def make_answer():
    player_name = get_name()
    progression = generate_progression()
    progression_hidden_element = randint(0, PROGRESSION_LEN - 1)
    print('Question:', end=' ')
    show_progression(progression, progression_hidden_element)
    answer = prompt.integer('Your answer : ')
    if answer == progression[progression_hidden_element]:
        print('Correct!')
        print(f'Congratulations, {player_name}!')
    else:
        wrong_answer_info(answer, progression[progression_hidden_element], player_name)


def main():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')
    welcome_user()
    make_answer()


if __name__ == "__main__":
    main()
