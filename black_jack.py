logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
import math


print(logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 


want = True 

def black_jack():
    ask = input('Hey do you want to play blackjack "y":yes "n":no ')
    if ask == 'y':
        user_card = [deal_card(), deal_card()]
        print(f'Your cards: {user_card} your score: {sum(user_card)}')
        computer_card = [deal_card(), deal_card()]
        print(f'computer_first_card : {computer_card[0]}')
        ask_2 = input('do you want to take another card "y" : yes, "n" : no ? ')
        if ask_2 == 'y':
            new = user_card.append(deal_card())
            print(f'new card: {new}')
        elif ask_2 == 'n':
            if sum(user_card) <= 21 and sum(user_card) > sum(computer_card):
                print('you won')
                black_jack()
            elif sum(user_card) > 21:
                print('you lost by exeding limit')
                black_jack()
            elif sum(user_card) <  sum(computer_card) and sum(computer_card) <= 21:
                print('computer won')
                black_jack()
            elif sum(computer_card) > 21:
                print('you won')
                black_jack()
    else:
        quit()


black_jack()
#kajfdjkasf