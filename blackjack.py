############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import blackjack_logo

play = input("Do you want to play a game of Blackjack? 'y' or 'n' ")
while play == "y":

    print(blackjack_logo)
    def player_hand():
        a = random.choice(cards)
        b = random.choice(cards)
        return [a, b]
    player_cards = player_hand()
    player_score = sum(player_cards)
    player_status = (f"Your cards: {player_cards}, current score: {player_score}")
    print(player_status)

    def dealer_hand():
        a = random.choice(cards)
        b = random.choice(cards)
        return [a, b]
    dealer_cards = dealer_hand()
    dealer_showing = dealer_cards[0]
    dealer_score = sum(dealer_cards)

    print(f"Computer\'s first card : {dealer_showing}")

    while player_score < 21:
        new_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if new_card == "y":
            c = random.choice(cards)
            player_cards.append(c)
            player_score = sum(player_cards)
            if player_score > 21:
                for player_card in player_cards:
                    if player_card == 11:
                        player_score = player_score - 10
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer\'s first card : {dealer_showing}")
        else:
            break
    # print(player_status)

    while dealer_score <= 21:
        if dealer_score < 15:
            c = random.choice(cards)
            dealer_cards.append(c)
            dealer_score = sum(dealer_cards)
            if dealer_score > 21:
                for dealer_card in dealer_cards:
                    if dealer_card == 11:
                        dealer_score = dealer_score - 10

        else:
            break

    print(f"Your final hand: {player_cards}, current score: {player_score}")
    print(f"Computer\'s final hand : {dealer_cards}, final score: {dealer_score}")

    if player_score > 21 and dealer_score > 21:
        print("Both players bust. No winners.")
    elif player_score == dealer_score:
        print("Draw. No winners.")
    elif player_score > 21 and dealer_score <= 21:
        print("You bust. Dealer wins.")
    elif dealer_score > 21 and player_score <= 21:
        print("Dealer busts. You win.")
    elif dealer_score > player_score:
        print("Dealer wins.")
    elif player_score > dealer_score:
        print("You win.")
    play = input("Do you want to play a game of Blackjack? 'y' or 'n' ")



# print(a, b)
# player_cards
# player_score = 
# dealer_cards
# dealer_score = 
#     def calculate_score(): and who wins
# convert 11 to 1 if total > 21

