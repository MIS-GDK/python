import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


ranks = [str(n) for n in range(2, 11)] + list("JQKA")
print(ranks)
suits = "spades diamonds clubs hearts".split()
print(suits)
# print([Card(rank, suit) for suit in suits for rank in ranks])

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

mycard = Card("8", "hearts")

print(FrenchDeck.ranks.index(mycard.rank))
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
print(suit_values)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


print(spades_high(mycard))
