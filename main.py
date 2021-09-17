import random
from art import logo


def computer_strategy(total_computer, hand_computer):
    """If the sum of the card of computer il less or equal 16 allow him to draw a card"""
    while total_computer <= 16:
        computer_cards = random.choice(cards)
        hand_computer.append(computer_cards)
        total_computer += computer_cards
        print(f"Tha computer hand {hand_computer},computer total cards {total_computer}")
        if 11 in hand_computer and total_computer > 21:
            hand_computer.remove(11)
            hand_computer.append(1)
            total_computer = sum(hand_computer)
    return total_computer


def compare_hands(total_hand_user, final_computer, hand_user, hand_computer,name_user):
    """Compare the score of the two player"""
    if total_hand_user > 21:
        return f"{hand_computer} My score is {final_computer}, {name_user} go bust computer win."
    elif total_hand_user == 21:
        return f"BlackJack I {name_user} "
    elif final_computer > 21:
        return f"{hand_user} {name_user} score is {total_hand_user}, computer busted"
    elif final_computer == 21:
        return "Blackjack computer win"
    elif total_hand_user < final_computer:
        return f"{hand_user} {name_user} total is {total_hand_user},{hand_computer} the computer hands score is {final_computer}\n You lose "
    elif total_hand_user > final_computer:
        return f"{hand_user} {name_user} score is {total_hand_user},{hand_computer} the computer score is {final_computer}\nYou win "
    else:
        return f"{hand_user} {name_user} score is {total_hand_user},{hand_computer} the computer score is {final_computer}\nWe draw "


def draw_card(total_hand_user, total_computer, hand_user, hand_computer,name_user):
    """Allow the user to draw a card if his score is too low"""
    draw = True
    while draw:
        draw = input(
            f"{name_user} hand is {hand_user} and your score is {total_hand_user} Do you like draw another card? 'draw' for "
            f"draw a card 'stay' for stay: ").lower()
        if draw == "draw":
            new_card = random.choice(cards)
            hand_user.append(new_card)
            total_hand_user += new_card
            print(f"{hand_user} the total is {total_hand_user}")
            if 11 in hand_user and total_hand_user > 21:
                hand_user.remove(11)
                hand_user.append(1)
                total_hand_user = sum(hand_user)
        elif draw == "stay":
            draw = False
            final_computer = computer_strategy(total_computer, hand_computer)
            final_score = compare_hands(total_hand_user, final_computer, hand_user, hand_computer,name_user)
            print(final_score)

print(logo)
print("Welcome to the BlackJack game")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7,
         8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game_begin():
    want_play = True
    name_user = input("Welcome what is your username? ")
    # Loop for check if the player wants to play
    while want_play:
        hand_user = []
        hand_computer = []
        start = input(f"Welcome {name_user} do you like to play a hand? Type 'yes' or 'no': ").lower()
        if start == "no":
            want_play = False
            print(f"Thanks {name_user} for play with me hope to see you soon!")
        elif start == "yes":
            for i in range(2):
                card_user = random.choice(cards)
                hand_user.append(card_user)
                total_hand_user = sum(hand_user)
                computer_cards = random.choice(cards)
                hand_computer.append(computer_cards)
                total_computer = sum(hand_computer)
            print(f"Your cards {hand_user}, the total score of your hand is {total_hand_user}")
            print(f"First card of computer {hand_computer[0]}")
            draw_card(total_hand_user, total_computer, hand_user, hand_computer,name_user)


game_begin()
