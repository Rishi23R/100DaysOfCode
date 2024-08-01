import random

game_over = False


def check_the_num(attempts, chosen_num, users_guess):
    if users_guess > chosen_num:
        print("Too high!")
        return attempts - 1


    elif users_guess < chosen_num:
        print("Too low")
        return attempts - 1

    else:
        print( f"you guessed it right with {attempts} chances left.The number is {chosen_num}")
        return

def play():
    print("Welcome to the number guessing game")
    print('Im choosing a number in between 1 and 100')
    chosen_num = random.choice(range(1, 100))
    difficulty_level = input("Chose your difficulty level easy or hard")
    if difficulty_level == 'easy':
        attempts = 10
    else:
        attempts = 5
    users_guess=0
    while users_guess!=chosen_num:
        print(f"you have{attempts} attempts left")
        users_guess=int(input('Make a guess:'))
        attempts=check_the_num(attempts,chosen_num,users_guess)
        if attempts==0:
            print(f'you have exhausted all your attempts.Correct number is {chosen_num}')
            return
        elif users_guess!=chosen_num:
            print("Guess again")

play()