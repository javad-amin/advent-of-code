import os

PROJECT_PATH: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH: str = os.path.join(PROJECT_PATH, "src", "input", "day_04.txt")


def get_number_of_matches(card: str) -> int:
    winning_numbers_str, my_numbers_str = card.split("|")
    winning_numbers = set(map(int, winning_numbers_str.split()))
    my_numbers = set(map(int, my_numbers_str.split()))
    return len(winning_numbers & my_numbers)


def calculate_total_cards(cards_data: list[str]) -> int:
    multipliers: list[int] = [1] * len(cards_data)

    for index, card in enumerate(cards_data):
        for offset in range(get_number_of_matches(card)):
            multipliers[index + offset + 1] += multipliers[index]

    return sum(multipliers)


def calculate_points(cards_data: list[str]) -> int:
    total_points: int = 0

    for card in cards_data:
        if matches := get_number_of_matches(card):
            total_points += 2 ** (matches - 1)

    return total_points


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        lines: list[str] = [line.strip() for line in f.readlines()]
        cards_data: list[str] = [line.split(":")[1] for line in lines]
    print(calculate_points(cards_data))
    print(calculate_total_cards(cards_data))
