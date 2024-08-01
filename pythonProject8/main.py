import random



def pick_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if (10 in cards) and (11 in cards):
        return 0
    if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
    return sum(cards)


def compare(user_score,computer_score):
    if user_score==computer_score:
        return 'its a draw'
    elif computer_score==0:
        return 'You lose'
    elif user_score==0:
        return 'you win'
    elif user_score>21:
        return 'You went over.You lose'
    elif computer_score>21:
        return 'Opponent went over you win'
    elif user_score>computer_score:
            return "you win"
    else:
        return 'you win'


def play_game():
    print('Welcome to blackjack')
    game_over = False
    user_cards=[]
    computer_cards=[]
    for _ in range(2):
        user_cards.append(pick_a_card())
        computer_cards.append(pick_a_card())


    while not game_over:
        print(user_cards)
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f'your cards are{user_cards}',f'computer\'s card is {computer_cards[0]}')
        if user_score == 0 or computer_score==0 or user_score>21:
            game_over=True
        else:
            did_game_end=input('You want to continue by drawing another card?')
            if did_game_end=='yes':
                user_cards.append(pick_a_card())
            else:
                game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(pick_a_card())
        computer_score=calculate_score(computer_cards)
    print(f"your final hand{user_cards},your final score{user_score}",
              f"computer's final hand {computer_cards},computer's final score{computer_score}")

    print(compare(user_score,computer_score))


while input('Do you want to play a game of blackjack type y to play')=='y':
    play_game()






