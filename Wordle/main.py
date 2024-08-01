import random
from hangman_art import stages,logo
from hangman_words import word_list
from replit import clear

chosen_word=random.choice(word_list)
lives=6
#Testing code
print(logo)
#print(f'Pssst, the solution is {chosen_word}.')
display=[]
for letter in chosen_word:
    display.append('_')
print(display)
word_guessed=False
guess_list=[]
while not word_guessed:
    guess=input('Guess a letter: ').lower()
    clear()
    guess_list.append(guess)
    if guess_list.count(guess) > 1:
        print('You\'ve already guessed that letter')
    if guess in chosen_word:
        for index,letter in enumerate(chosen_word):
            if guess ==letter:
                display[index]=letter
    else:
        lives-=1
        print('You guessed a letter that\'s not in the word.You lose a life')
        if lives==0:
            word_guessed=True
            print('You lose')
            print(f'The word is {chosen_word}')
    print(stages[lives])


    print(display)
    if '_' not in display:
        word_guessed=True
        print("you've won")
