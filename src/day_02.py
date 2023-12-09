import operator
import os
from functools import reduce

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(PROJECT_PATH, "src", "input", "day_02.txt")

ACTUAL_BAG_WITH_CUBES = {"red": 12, "green": 13, "blue": 14}


def sum_of_game_ids_possible_with_bag(games_parsed: list[list[dict[str, int]]]) -> int:
    return sum(
        game_index + 1
        for game_index, game_rounds in enumerate(games_parsed)
        if all(
            cube_value <= ACTUAL_BAG_WITH_CUBES.get(cube_color, 0)
            for game_round in game_rounds
            for cube_color, cube_value in game_round.items()
        )
    )


def sum_of_powers_minimum_to_pass(games_parsed: list[list[dict[str, int]]]) -> int:
    return sum(
        reduce(
            operator.mul,
            {
                color: max(game_round.get(color, 0) for game_round in game_rounds)
                for color in ["red", "green", "blue"]
            }.values(),
        )
        for game_rounds in games_parsed
    )


def parse_games_data(lines: list[str]) -> list[list[dict[str, int]]]:
    games_data = [line.strip().split(":")[1] for line in lines]
    games_rounds = [round.strip().split(";") for round in games_data]

    games_parsed = [
        [
            {
                cube_data.strip().split(" ")[1]: int(cube_data.strip().split(" ")[0])
                for cube_data in game_round.strip().split(",")
            }
            for game_round in game_rounds
        ]
        for game_rounds in games_rounds
    ]

    return games_parsed


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        parsed_games = parse_games_data(f.readlines())

        print(sum_of_game_ids_possible_with_bag(parsed_games))
        print(sum_of_powers_minimum_to_pass(parsed_games))
