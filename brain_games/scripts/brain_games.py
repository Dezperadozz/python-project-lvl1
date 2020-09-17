import prompt


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def main():
    greet()
    welcome_user()


if __name__ == "__main__":
    main()
