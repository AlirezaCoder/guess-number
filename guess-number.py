from random import randint
number = 0
guess_chance = 10


def check_user_input(_user_input):
    if not _user_input:
        print("please enter valid number")
        return False
    elif not _user_input.isnumeric():
        print("please enter only a number")
        return False
    elif not 1 <= int(_user_input) <= 50:
        print("please enter a number between 1 and 50")
        return False
    return True


def intialize_game():
    global number, guess_chance
    number = randint(1, 50)
    guess_chance = 10


def try_again():
    print("do you want to play again?")
    user_answer = input()
    if user_answer.lower() in ["y", "yes"]:
        intialize_game()
    else:
        print("GOOD BY!")
        exit()


intialize_game()
while True:
    print("please guess a number between 1 and 50")
    print("chance: " + str(guess_chance))
    user_number = input()
    if not check_user_input(user_number):
        continue
    user_number = int(user_number)
    if user_number == number:
        print("your guess is true. the number is " + str(number))
        try_again()

    elif user_number != number:
        guess_chance -= 1
        if guess_chance == 0:
            print("you could not guess the number. your chances are finished.")
            print("the number was: " + str(number))
            try_again()
        elif number < user_number:
            print("the number is smaller than your guess")
        else:
            print("the number is larger than your guess")
