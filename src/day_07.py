import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(PROJECT_PATH, "src", "input", "day_07.txt")


class Hand:
    def __init__(self, cards, bid, strength, joker_rule=False):
        self.cards = cards
        self.bid = bid
        self.strength = strength
        self.joker_rule = joker_rule

    def card_to_number(self, card):
        if card.isdigit():
            return int(card)
        return {
            "J": 1 if self.joker_rule else 11,
            "T": 10,
            "Q": 12,
            "K": 13,
            "A": 14,
        }[card]

    def __lt__(self, other):
        if self.strength != other.strength:
            return self.strength < other.strength
        for card_self, card_other in zip(self.cards, other.cards):
            if card_self != card_other:
                return self.card_to_number(card_self) < self.card_to_number(card_other)
        return False


def get_counts_with_joker(hand_cards, counts):
    joker_count = hand_cards.count("J")

    joker_map = {
        4: {"default": [5]},
        3: {(3, 2): [5], "default": [4, 1]},
        2: {(3, 2): [5], (2, 2, 1): [4, 1], "default": [3, 1, 1]},
        1: {
            (4, 1): [5],
            (3, 1, 1): [4, 1],
            (2, 2, 1): [3, 2],
            (2, 1, 1, 1): [3, 1, 1],
            "default": [2, 1, 1, 1],
        },
    }

    if joker_count in joker_map:
        return joker_map[joker_count].get(
            tuple(counts), joker_map[joker_count]["default"]
        )
    return counts


def parse_hand(line, joker_rule=False):
    hand_cards, hand_bid = line.split()[0], int(line.split()[1])
    counts = [hand_cards.count(card) for card in set(hand_cards)]
    counts.sort(reverse=True)

    if joker_rule:
        counts = get_counts_with_joker(hand_cards, counts)

    hand_map = {
        (5,): 7,
        (4, 1): 6,
        (3, 2): 5,
        (3, 1, 1): 4,
        (2, 2, 1): 3,
        (2, 1, 1, 1): 2,
        (1, 1, 1, 1, 1): 1,
    }

    if tuple(counts) in hand_map:
        return Hand(hand_cards, hand_bid, hand_map[tuple(counts)], joker_rule)

    raise ValueError(f"Unknown hand type: {counts}, {hand_cards=}")


def total_winnings(lines, joker_rule=False):
    hands = [parse_hand(line, joker_rule) for line in lines]
    hands.sort()
    total_winnings = sum(hand.bid * (i + 1) for i, hand in enumerate(hands))
    print(total_winnings)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        lines = [line.strip() for line in f.readlines()]
    total_winnings(lines)
    total_winnings(lines, joker_rule=True)
