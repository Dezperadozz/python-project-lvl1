import prompt

ROUNDS = 3
PLAYERS = []


def show_wrong_answer_info(answer, correct_answer, player_name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {player_name}!")


def show_confirmation():
    print('Correct!')


def congratulate_player(player_name):
    print(f'Congratulations, {player_name}!')


def input_answer():
    answer = prompt.integer('Your answer : ')
    return answer


def greet():
    print('Welcome to the Brain Games!')


def add_player(name):
    PLAYERS.append(name)


def get_player_name(player_number=0):
    return PLAYERS[player_number]
