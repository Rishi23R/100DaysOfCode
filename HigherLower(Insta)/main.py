#print the welcome logo
#two random choices should be taken from the list
#print the two against each other
#take users guess and check if its right or not
#if its right then replace the first choice with the second one and the second one with a new one
# and continue the game
#if its wrong give user his score and end the game
import random
from game_data import data
from art import logo, vs


def compare(first_choice, second_choice):
    follower_a = first_choice['follower_count']
    follower_b = second_choice['follower_count']
    #print(follower_a,follower_b)
    print(f"Compare A: {first_choice['name']}, a {first_choice['description']} from {first_choice['country']}")
    print(vs)
    print(f"Against B: {second_choice['name']}, a {second_choice['description']} from {second_choice['country']}")
    if follower_a > follower_b:
        return "A"
    return "B"


def user_accuracy(right_answer):
    user_guess = input("Who has more followers? Type 'A' or 'B':").upper()
    if user_guess == right_answer:
        return 1
    return 0


def play():
    score = 0
    print(logo)
    print("Welcome to HigherLower Instagram version\nAll you gotta do is guess who has more number of followers.Have fun!")
    first_choice = random.choice(data)
    second_choice = random.choice(data)
    right_answer = compare(first_choice, second_choice)
    game_continuity = user_accuracy(right_answer)

    while game_continuity:
        score += 1
        first_choice = second_choice
        second_choice = random.choice(data)
        right_answer = compare(first_choice, second_choice)
        game_continuity = user_accuracy(right_answer)
    print(f'Sorry you lose.Your score is {score}')


play()