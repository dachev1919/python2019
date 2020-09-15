import collections 
from random import *

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        print(self._cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

if __name__ == "__main__":
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    deck = FrenchDeck()
    print("В колоде ", len(deck), "карты")
    num = choice(deck)
    print("Вам выпала карта -> ", num[0] + ' ' + num[1], end="")
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    for card in sorted(deck, key=spades_high):
        print(card)