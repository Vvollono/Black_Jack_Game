# Black_Jack_Game
Code and README file for the Blackjack game I create

#Blacjack Game

The goal of this exercise is to create a simple version of Blackjack game where the user challenge the computer.

#Rule of the game

1)The deck is unlimited size.
2)There are no jokers.
3)The Jack/Queen/King all count as 10.
4)The Ace can count as 1 or 11.
5)Card list card = [11,2,3,4,5,6,7,8,9,10,10,10,10].
6)The cards on the list have equal probability to be drawn.
7)Cards are not removed from the deck as they are drawn.

#Breakdown project

1)Deal both user and computer a starting hand of 2 random card values.

2)Detect when computer or user has a blackjack. (Ace + 10 value card).

3)If computer gets blackjack, then the user loses (even if the user also has a blackjack). If the user gets a blackjack, then they win (unless the computer also has a blackjack).

4)Calculate the user's and computer's scores based on their card values.

5)If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.

6)Reveal computer's first card to the user.

7)Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.

8)Ask the user if they want to get another card.

9)Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep drawing cards unless their score goes over 16.

10)Compare user and computer scores and see if it's a win, loss, or draw.

11)Print out the player's and computer's final hand and their scores at the end of the game.

12)After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.

#Goal of exercise 

Use the knowledge I have acquired so far on the loop, condition, list and function for create a working game.
