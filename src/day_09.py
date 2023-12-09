import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(PROJECT_PATH, "src", "input", "day_09.txt")


def extrapolate_previous(sequences: list[list[int]]) -> int:
    sequences[-1].insert(0, 0)
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].insert(0, sequences[i][0] - sequences[i + 1][0])
    return sequences[0][0]


def extrapolate_next(sequences: list[list[int]]) -> int:
    sequences[-1].append(0)
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
    return sequences[0][-1]


def calculate_differences(sequence: list[int]) -> list[int]:
    return [b - a for a, b in zip(sequence, sequence[1:])]


def generate_sequences(sequence: list[int]) -> list[list[int]]:
    sequences = [sequence]
    while not all(value == 0 for value in sequences[-1]):
        sequences.append(calculate_differences(sequences[-1]))
    return sequences


def predict_value(sequence: list[int], direction="next") -> int:
    sequences = generate_sequences(sequence)
    if direction == "next":
        return extrapolate_next(sequences)
    elif direction == "previous":
        return extrapolate_previous(sequences)
    return 0


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        lines = [list(map(int, line.strip().split())) for line in f.readlines()]
    print(sum(predict_value(line, "next") for line in lines))
    print(sum(predict_value(line, "previous") for line in lines))
