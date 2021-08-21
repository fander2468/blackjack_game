# Python Blackjack
# For this project you will make a Blackjack game using Python. 

# Rules:
# 1. The game will have two players: the Dealer and the Player. The game will start off with a deck of 52 cards. The 52 cards will consist of 4 different suits: Clubs, Diamonds, Hearts and Spades. For each suit, there will be cards numbered 1 through 13.

# Note: No wildcards will be used in the program
# 2. When the game begins, the dealer will shuffle the deck of cards, making them randomized. After the dealer shuffles, it will deal the player 2 cards and will deal itself 2 cards from. The Player should be able to see both of their own cards, but should only be able to see one of the Dealer's cards.

# 3. The objective of the game is for the Player to count their cards after they're dealt. If they're not satisfied with the number, they have the ability to 'Hit'. A hit allows the dealer to deal the Player one additional card. The Player can hit as many times as they'd like as long as they don't 'Bust'. A bust is when the Player is dealt cards that total more than 21.

# 4. If the dealer deals the Player cards equal to 21 on the first deal, the Player wins. This is referred to as Blackjack. Blackjack is NOT the same as getting cards that equal up to 21 after the first deal. Blackjack can only be attained on the first deal.

# 5. The Player will never see the Dealer's hand until the Player chooses to 'stand'. A Stand is when the player tells the dealer to not deal it anymore cards. Once the player chooses to Stand, the Player and the Dealer will compare their hands. Whoever has the higher number wins. Keep in mind that the Dealer can also bust.

# Imports that will be needed for the app
import random 
import os

# Player class
class Player():
    def __init__(self, player_cards = [], dealer_cards = []):
        self.player_cards = player_cards
        self.dealer_cards = dealer_cards

    # player cards 
    def player(self):
        # self.player_cards = getattr(Card, self.player_cards)
        self.player_cards = Cards.deal_two_cards(self)

    # dealer cards
    def dealer(self):
        # self.dealer_cards = getattr(Card, self.dealer_cards)
        self.dealer_cards = Cards.deal_two_cards(self)

    # player decisons method - player can hit, stand
    def player_decision(self, player_input):
        if player_input == 'hit'.lower() and Cards.count > 0:
            self.player_cards = Cards.deal_one_card(self)
            return True
        elif player_input == 'stay'.lower():
            print("Player decided to stay and doesn't want anymore cards'.")

    def dealer_decison(self, player_input):
        if sum(self.dealer_cards) < 17 and player_input == 'stay'.lower():
            self.dealer_cards.append(Cards.deal_one_card())
        
    # method to work with face cards 
    def card_face(self):
        for i in self.player_cards:
            if i == 'jack' or i == 'queen' or i == 'king':
                self.player_cards[i] = 10

    # method to work with ace card 
    def card_ace(self):
        for i in self.player_cards:
            if i == 'ace' and sum(self.player_cards) >= 11:# Need to fix this line
                self.player_cards[i] = 1
            else:
                self.player_cards[i] = 11

 








# Card class
class Cards():
    def __init__(
        self,
        cards = ["ace" ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,"jack" ,"queen" ,"king"],
        card_suit = ["clubs", "hearts", "diamonds", "spades"],
        cards_choices = [], count = 52):
        self.cards = cards
        self.cards_suit = card_suit
        self.cards_choices = cards_choices
        self.count = count

    

    # cards/list can be shuffled randomly each time a new game is played 
    def shuffled(self):
        random.shuffle(self.cards)

    # deal two cards from the deck after cards are shuffled to both player and dealer
    def deal_two_cards(self):
        for i in range(2):
            self.cards_choices.random.choice(self.cards)

    # deal one card from the deck each time a hit is called
    def deal_one_card(self):
        for i in range(1):
            self.cards_choices.append(random.choice(self.cards))

    def remove_card_from_deck(self):
        if Player.player_decision == True:
            self.count -= 1
    



    





class Board():
    def __init__(self, board):
        self.board = board
    
    def start_game(self):
        pass

    # show method for cards; can compare dealer with player
    def show(self):
        pass
    
    def win(self):
       pass

    def turn(self):
       pass    

