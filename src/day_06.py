import os

PROJECT_PATH: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH: str = os.path.join(PROJECT_PATH, "src", "input", "day_06.txt")


def calculate_ways_to_win(time: int, distance: int) -> int:
    max_distances: list[int] = [(time - i) * i for i in range(time + 1)]
    return sum(d > distance for d in max_distances)


def concatenate_times_and_distances(lines: list[str]) -> tuple[int, int]:
    time: int = int("".join(lines[0].split()[1:]))
    distance: int = int("".join(lines[1].split()[1:]))
    return time, distance


def calculate_total_ways_to_win(times: list[int], distances: list[int]) -> int:
    ways_to_win: list[int] = [
        calculate_ways_to_win(time, distance)
        for time, distance in zip(times, distances)
    ]
    total_ways: int = 1
    for way in ways_to_win:
        total_ways *= way
    return total_ways


def parse_times_and_distances(lines: list[str]) -> tuple[list[int], list[int]]:
    times: list[int] = list(map(int, lines[0].split()[1:]))
    distances: list[int] = list(map(int, lines[1].split()[1:]))
    return times, distances


def read_input() -> list[str]:
    with open(INPUT_PATH) as f:
        lines: list[str] = [line.strip() for line in f.readlines()]
    return lines


if __name__ == "__main__":
    lines: list[str] = read_input()
    times, distances = parse_times_and_distances(lines)
    total_ways: int = calculate_total_ways_to_win(times, distances)
    print(total_ways)

    time, distance = concatenate_times_and_distances(lines)
    ways_to_win: int = calculate_ways_to_win(time, distance)
    print(ways_to_win)
