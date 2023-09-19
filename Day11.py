##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

# Blackjack is a popular card game played in casinos around the world. 
# The objective of the game is to beat the dealer by having a hand value that is closer to 21 than the dealer's hand, without exceeding 21. 
# Here's Blackjack:


import random


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')
    return deck


def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card.split()[0]
        value += values[rank]
        if rank == 'Ace':
            aces += 1
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value


def display_hand(player, hand):
    print(f"{player}'s Hand:")
    for card in hand:
        print(card)
    print(f'Total Value: {calculate_hand_value(hand)}\n')


deck = create_deck()
random.shuffle(deck)
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

print("Welcome to Blackjack!")
display_hand("Player", player_hand)
display_hand("Dealer", [dealer_hand[0], 'Hidden Card'])


while calculate_hand_value(player_hand) < 21:
    action = input("Do you want to 'Hit' or 'Stand'? ").lower()
    if action == 'hit':
        player_hand.append(deck.pop())
        display_hand("Player", player_hand)
    elif action == 'stand':
        break


while calculate_hand_value(dealer_hand) < 17:
    dealer_hand.append(deck.pop())


print("Final Hands:")
display_hand("Player", player_hand)
display_hand("Dealer", dealer_hand)


player_value = calculate_hand_value(player_hand)
dealer_value = calculate_hand_value(dealer_hand)
if player_value > 21:
    print("Player busts! Dealer wins.")
elif dealer_value > 21:
    print("Dealer busts! Player wins.")
elif player_value > dealer_value:
    print("Player wins!")
elif dealer_value > player_value:
    print("Dealer wins.")
else:
    print("It's a tie!")

print("Thanks for playing!")


#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################