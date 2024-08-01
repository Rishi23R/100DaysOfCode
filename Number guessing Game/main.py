#print the logo and welcome msg
#ask use to chose difficulty level
#no of attempts based on difficulty level
#create a loop where user keeps guessing till he is right or attempts come
#down to zero whichever happens first
import random

#def guess_game(attempts):
#for _ in range(attempts):
#pass


print('Welcome to the number guessing game')
print('Im choosing a number in between 1 and 100')
chosen_num = random.choice(range(1, 100))
print(chosen_num)
difficulty_level = input("Chose your difficulty level easy or hard")
if difficulty_level == 'easy':
    attempts = 10
else:
    attempts = 5

while attempts > 0:
    print(f"you have {attempts} guesses left")
    users_guess = int(input('Make a guess:'))
    if users_guess > chosen_num:
        print("Too high!\nGuess again")
        attempts -= 1
    elif users_guess < chosen_num:
        print("Too low\nGuess again")
        attempts -= 1
    else:
        print(f"you guessed it right with {attempts} chances left.The number is {chosen_num}")
        break
