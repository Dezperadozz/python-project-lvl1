import prompt

NAME = None


def get_name():
    return NAME


def welcome_user():
    global NAME
    if get_name() is None:
        NAME = prompt.string('May I have your name? ')
    print(f'Hello, {NAME}!')
    print()