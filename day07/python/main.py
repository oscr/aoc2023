import enum
from collections import Counter
from functools import total_ordering


@total_ordering
class Card:
    card_value = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10
    }

    def __init__(self, value, joker=False):
        self.joker = joker
        if value in self.card_value:
            if joker and value == 'J':
                self.value = 1
            else:
                self.value = int(self.card_value[value])
        else:
            self.value = int(value)

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented

    def __str__(self):
        if self.value < 10:
            return str(self.value)
        else:
            for k, v in self.card_value.items():
                if self.value == v:
                    return k

    def is_joker(self):
        return self.value == 1


@total_ordering
class HandType(enum.Enum):
    Five = 6
    Four = 5
    FullHouse = 4
    Three = 3
    TwoPair = 2
    Pair = 1
    High = 0

    @staticmethod
    def get_handtype(cards, joker=False):
        c = Counter([str(c) for c in cards])

        if joker:
            del c['1']
            if c:
                sorted(c, reverse=True)
                key, value = c.most_common()[0]
                c.update({key: len([c for c in cards if c.is_joker()])})
            else:
                return HandType.Five

        card_type_count = len(c.keys())
        if card_type_count == 1:
            return HandType.Five
        elif card_type_count == 2:
            if any([v == 4 for _, v in c.most_common()]):
                return HandType.Four
            else:
                return HandType.FullHouse
        elif card_type_count == 3:
            if any([v == 3 for _, v in c.most_common()]):
                return HandType.Three
            else:
                return HandType.TwoPair
        elif card_type_count == 4:
            return HandType.Pair
        else:
            return HandType.High

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    def __str__(self):
        return str(self.value)


@total_ordering
class Hand:
    def __init__(self, cards, bid, joker=False):
        self.joker = joker
        self.type = HandType.get_handtype(cards, joker)
        self.cards = cards
        self.bid = bid

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            if self.type != other.type:
                return self.type < other.type
            else:
                for i, card in enumerate(self.cards):
                    if card != other.cards[i]:
                        return card < other.cards[i]
                print("Same cards found..")

    def __str__(self):
        return str([str(c) for c in self.cards])


def solve(hands):
    result = 0
    for i, hand in enumerate(hands, start=1):
        result += i * hand.bid
    return result


def parse_input(filename, joker=False):
    lines = open(filename, 'r').read().splitlines()
    hands = []
    for line in lines:
        str_cards, str_bid = line.split(" ")
        cards = [Card(s, joker) for s in str_cards]
        hands.append(Hand(cards, int(str_bid), joker))
    hands.sort()
    return hands


if __name__ == "__main__":
    assert solve(parse_input('../input_example.txt')) == 6440
    assert solve(parse_input('../input_example.txt', True)) == 5905
    assert solve(parse_input('../input.txt')) == 250232501
    assert solve(parse_input('../input.txt', True)) == 249138943