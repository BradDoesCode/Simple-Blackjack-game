import random

# ===========================================
#  Simple Text based blackjack game
# ===========================================
# Global variables used for deck creation
game_on = True

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


# ===========================================
# Classes
# ===========================================


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        # empty list to hold the deck
        self.all_cards = []
        # deck creation using the Card class
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        # we remove one card from the list of all_cards
        return self.all_cards.pop(0)


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        return f"{self.name}, {[card.__str__() for card in self.hand]}, Total: {self.value}"

    def add_card(self, card):
        self.hand.append(card)
        # check if card is an ace
        if card.rank == 'Ace':
            self.aces += 1
        # update the hand value
        self.add_value(card.value)

    def add_value(self, value):
        self.value += value
        # adjust for ace if available and hand value is over 21
        if self.value > 21 and self.aces > 0:
            self.aces -= 1
            self.value -= 10

    def turn(self):
        while self.value < 21:
            try:
                choice = input('Would you like to hit or stand? ').lower()
                if choice[0] == 'h':
                    # add card to hand and print new hand
                    self.add_card(new_deck.deal_one())
                    print(self.__str__())
                elif choice[0] == 's':
                    break
                else:
                    continue
            except ValueError:
                continue

    def reset(self):
        # resets values for new round
        self.hand = []
        self.aces = 0
        self.value = 0


class Bank:

    def __init__(self, balance=0):
        self.balance = balance

    def __str__(self):
        return f"Current chip balance: {self.balance}"

    def place_bet(self):
        while True:
            try:
                bet = int(input('How much do you want to bet? '))
                # check for valid bet
                if bet <= self.balance:
                    self.balance - bet
                    break
                print('please enter valid amount')
            except ValueError:
                print("Please enter valid amount")
        return bet

    def win_bet(self, amount):
        self.balance += amount * 2

def player_win():
    print(dealer)
    # check if player is bust
    if player_one.value > 21: return 'Loss'
    # dealer hits until dealer value is >= player
    while dealer.value < player_one.value:
        dealer.add_card(new_deck.deal_one())
        print(dealer)
    # check if player draws
    if dealer.value == player_one.value: return 'Draw'
    # check if player wins
    if dealer.value > 21:
        return 'Win'
    return 'Loss'

def play_again():
    answer = input('Would you like to play again? ').lower()
    if answer[0] != 'y':
        # stop the game if player enters anything but y
        global game_on
        game_on = False
    # reset player and dealer values for new round
    player_one.reset()
    dealer.reset()



if __name__ == "__main__":
    # setup player and dealer
    player_one, player_bank = Player(input('What is your name? ')), Bank(int(input('How much do you wish to deposit? ')))
    dealer = Player('dealer')


    while game_on:
        # create new deck and shuffle
        new_deck = Deck()
        new_deck.shuffle()
        # print player balance and ask for bet amount
        print(player_bank)
        current_bet = player_bank.place_bet()
        # deal cards for each player and display them
        for x in range(0, 2):
            player_one.add_card(new_deck.deal_one())
            dealer.add_card(new_deck.deal_one())
        print(player_one)
        print('Dealers hand')
        print(dealer.hand[0], '')

        player_one.turn()

        # plays dealers turn and checks for a winner.
        match player_win():
            case 'Win':
                player_bank.win_bet(current_bet)
                print(f"{player_one.name} Wins! £{current_bet * 2} added to bank. New Balance: {player_bank.balance}")
            case 'Loss':
                print(f"Dealer wins!")
            case 'Draw':
                print(f'Its a draw! returned bet of {current_bet}')
        play_again()
        
