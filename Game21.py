import random

suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
rank_to_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

playing = True


class Card:
# creeaza toate cartile
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
# creeaza pachetul de carti
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_combination = ''
        for card in self.deck:
            deck_combination += '\n ' + card.__str__()
        return 'The deck has: ' + deck_combination
# amesteca cartile
    def shuffle(self):
        random.shuffle(self.deck)
# alege o carte din pachet
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Player:
# arata toate cartile pe care le are jucatorul
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.total = 100
        self.bet = 0
# alege carte pentru jucator
    def add_card(self, card):
        self.cards.append(card)
        self.value += rank_to_value[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
# colecteaza castigul
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def tie_bet(self):
        self.total == self.bet


class Dealer:

    def __init__(self):
        self.total = 100
        self.bet = 0
        self.cards = []
        self.value = 0
        self.aces = 0
# alege carte pentru dealer
    def add_card(self, card):
        self.cards.append(card)
        self.value += rank_to_value[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Invalid number: ")
        else:
            if chips.bet > chips.total:
                print("You cannot bet more than 100 chips!")
            else:
                break

# alege carte cand introduce hit
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stay(deck, hand):
    global playing

    while True:
        ask = input("\nWould you like to hit or stay? Enter 'h' for hit or 's' for stay: ")

        if ask[0].lower() == 'h':
            hit(deck, hand)
        elif ask[0].lower() == 's':
            print("Player stands, Dealer is playing.")
            playing = False
        else:
            print("Please try again!")
            continue
        break

# arata cartile la inceputul jocului, pentru jucator si dealer
def show_some(player, dealer):
    print("\nDealer's Hand: ")
    print(" <card hidden>") # carte ascunsa pentru dealer
    print("", dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')

# arata cartile la sfarsitul jocului
def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


# sfarsitul jocului

def player_busts(player, dealer, chips):
    print("PLAYER BUSTS!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("DEALER BUSTS!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()


def push(player, dealer):
    print("Its a push! Player and Dealer tie!")


# jocul

while True:
    print("Welcome to BlackJack!")

    # amesteca cartile
    deck = Deck()
    deck.shuffle()

    player_hand = Player()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Player()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # chips
    player_chips = Dealer()

    # pariul
    take_bet(player_chips)

    # arata cartile
    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stay(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

    print("\nPlayer's winnings stand at", player_chips.total)

    new_game = input("\nWould you like to play again? Enter 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\nThank you for playing!")
        break