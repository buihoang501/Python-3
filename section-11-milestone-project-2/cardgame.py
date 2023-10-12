import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Cart:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# ba bích
three_spade = Cart("Spades", "Three")
# print  Three of Spade by __str__
print(three_spade)

print(three_spade.value)


# Desk Class
class Deck:

    def __init__(self):
        # Empty list cards
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # init card
                created_card = Cart(suit, rank)
                # add card to list
                self.all_cards.append(created_card)
    # shuffle 52 cards

    def shuffle(self):
        random.shuffle(self.all_cards)
    # grabbing one card

    def deal_one(self):
        return self.all_cards.pop()


new_deck = Deck()
print(new_deck.all_cards)

first_cart = new_deck.all_cards[0]

print(first_cart)
# two of Hearts  by Card method __str__

last_cart = new_deck.all_cards[-1]
print(last_cart)

for card in new_deck.all_cards:
    print(card)
print(len(new_deck.all_cards))

new_deck.shuffle()
last_cart = new_deck.all_cards[-1]
print(last_cart)

my_card = new_deck.deal_one()
print('I have just grabbed {}'.format(my_card))

# remainder of cards
print(len(new_deck.all_cards))


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # add mutiple cards
            self.all_cards.extend(new_cards)
        else:
            # add one card
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


new_player = Player("Hoang")
print(new_player)

new_player.add_cards(my_card)
# player after adding cards
print(new_player)
print(new_player.all_cards[0])
print('\n')
print(f'current {my_card}')
new_player.add_cards([my_card, my_card, my_card])
print(new_player)
for player_card in new_player.all_cards:
    print(player_card)
new_player.remove_one()
print(len(new_player.all_cards))


# Game Setup
player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

# Game on
round_num = 0
while game_on:
    round_num += 1
    print(f"Current round {round_num}")

    # game role
    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One Wins!')
        game_on = False
        break

    # Start a new round
    # Get cards for player 1
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    # Get cards for player 2
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # while at_war
    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False
        else:
            print('Wars!')

            if len(player_one.all_cards) < 5:
                print('Player One Unable To Declare War')
                print('Player Two Wins!')
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print('Player Two Unable To Declare War')
                print('Player One Wins!')
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
