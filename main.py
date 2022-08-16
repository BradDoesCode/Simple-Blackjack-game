import random
# ===========================================
#  Simple Text based blackjack game
# ===========================================
# Global variables used for deck creation
playerturn = True

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
         'Queen': 10, 'King': 10, 'Ace': 11}

# ===========================================
# Classes
# ===========================================


class Card:

    def __init__(self,suit,rank):
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
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        # we remove one card from the list of all_cards
        return self.all_cards.pop(0)

class Player:

    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
        self.hand = []

    def __str__(self):
        return self.name + ", your balance is " + str(self.balance)

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
            return True
        return False

    def add_card(self, new_card):
        self.hand.append(new_card)

    def stand(self):
        pass

    def take_bet(self, amount):
        self.balance -= amount

# ===========================================
# Functions
# ===========================================



def display_rules():
    print('Rules displayed!')

def setup_player():

    while True:
        try:
            player_name = input('Please Enter a username: ')
            if not player_name:
                raise ValueError('Empty String')
        except ValueError as e:
            print(e)
        else:
            break
    while True:
        try:
            player_deposit = int(input('Enter deposit amount: '))
        except ValueError:
            print('Please enter a valid amount.')
        else:
            break
    playerone = Player(player_name,player_deposit)
    return playerone


def place_bet():
    while True:
        try:
            amount = int(input(f'Your current balance is: {playerone.balance}. Please enter bet amount: '))
        except ValueError:
            print('Please enter a valid amount. ')
        else:
            if amount > playerone.balance:
                print('Insufficient funds')
                continue
            else:
                playerone.take_bet(amount)
                break
    return amount

def display_hands():
    print(f'\n{playerone.name}, your hand is: ')
    value = 0
    for card in playerone.hand:
        print(card)
        value += card.value
    print(f'Hand value : {value}')

    print(f"\nThe Dealer has a: \n{dealer.hand[0]}\n")

def check_bust():
    global playerturn
    value = 0
    ace_in_hand = 0
    for card in playerone.hand:
        value += card.value

    if value <= 21:
        return False
    elif value > 21:
        for card in playerone.hand:
           if card.value == 11:
                card.value = 1
                return False

    playerturn = False
    return True




def player_choice():
    player_choice = ""
    while True:
        try:
            player_choice = input(f'Your turn {playerone.name}, would you like to hit or stand?').upper()
            if not player_choice:
                raise ValueError('Empty string')
        except ValueError as e:
            print(e)
        else:
            return player_choice

def keep_playing():
    player_action = None
    while True:
        player_action = input('Press Enter to keep playing or you can deposit/withdraw').lower()
        if player_action == "":
            dealer.hand = []
            playerone.hand = []
            return True
        elif player_action =='withdraw':
            playerone.withdraw(playerone.balance)
            return False
        elif player_action == 'deposit':
            while True:
                try:
                    amount = int(input(f'Your current balance is £{playerone.balance}. Please Enter Deposit anount: '))
                except ValueError:
                    print('Enter valid number')
                else:
                    playerone.deposit(amount)
                    dealer.hand = []
                    playerone.hand = []
                    return True
# ===========================================
# Main Logic
# ===========================================

def main():
    global playerturn
    while True:
        round = 0
        display_rules()
        new_deck = Deck()
        new_deck.shuffle()
        game_on = True
        while game_on:
            # player to place bet
            round += 1
            stake = place_bet()
            # deal the hand


            for x in range(2):
                playerone.add_card(new_deck.deal_one())
                dealer.add_card(new_deck.deal_one())

            # players turn
            playerturn = True
            while playerturn:

                print(f'This is round {round}')
                display_hands()
                player_move = player_choice()
                if player_move == 'HIT':
                    playerone.add_card(new_deck.deal_one())
                    if check_bust():
                        playerturn == False
                if player_move == 'STAND':
                    playerturn = False
            # dealers turn
            if not check_bust():
                print('Dealers hand: ')
                players_value = 0
                dealers_value = 0
                for card in playerone.hand:
                    players_value += card.value

                for dcard in dealer.hand:
                    print(dcard)
                    dealers_value += dcard.value

                while dealers_value < players_value:

                    newcard = new_deck.deal_one()
                    dealer.add_card(newcard)
                    print(newcard)
                    dealers_value += newcard.value
                    if dealers_value > 21:
                        for cards in dealer.hand:
                            if cards.value == 11:
                                cards.value = 1
                                break

                if dealers_value > 21:
                    print(f'Dealer loses! {stake*2} added to account!')
                    playerone.deposit(stake*2)

                elif dealers_value == players_value:
                    print(f'Its a draw! {stake} added to balance')
                    playerone.deposit(stake)

                elif dealers_value > players_value and dealers_value <= 21:
                    print(f'Dealer Wins! {playerone.name}: {players_value}. {dealer.name}: {dealers_value}. £{stake} lost!')

                print(f'{playerone.name} scored: {players_value}, The Dealer has: {dealers_value} ')


            else:
                for card in playerone.hand:
                    print(card)
                print(f'You bust! £{stake} lost')

            if not keep_playing():
                game_on = False
        break


if __name__ == '__main__':

    playerone = setup_player()
    dealer = Player('Dealer', 100000)
    main()