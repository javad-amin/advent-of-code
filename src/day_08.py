import math
import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(PROJECT_PATH, "src", "input", "day_08.txt")


def navigate_desert_lcm(
    instructions: list[str], positions: dict[str, tuple[str, ...]]
) -> int:
    start_positions = [position for position in positions if position.endswith("A")]
    lcm = 1

    for start in start_positions:
        position = start
        steps = 0
        instruction_index = 0

        while not position.endswith("Z"):
            instruction = instructions[instruction_index]
            instruction_index = (instruction_index + 1) % len(instructions)
            position = positions[position][0 if instruction == "L" else 1]
            steps += 1

        lcm = math.lcm(lcm, steps)

    return lcm


def navigate_desert(
    instructions: list[str], positions: dict[str, tuple[str, ...]]
) -> int:
    current_position = "AAA"
    steps = 0
    instruction_index = 0

    while current_position != "ZZZ":
        instruction = instructions[instruction_index]
        instruction_index = (instruction_index + 1) % len(instructions)

        next_position = positions[current_position][0 if instruction == "L" else 1]
        current_position = next_position
        steps += 1

    return steps


def parse_file(lines: list[str]) -> tuple[list[str], dict[str, tuple[str, ...]]]:
    instructions = list(lines[0])
    position_map = {}

    for line in lines[2:]:
        current_position, left_right_positions = line.split(" = ")
        position_map[current_position] = tuple(
            left_right_positions.strip("()").split(", ")
        )
    return instructions, position_map


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        lines = [line.strip() for line in f.readlines()]
    instructions, positions = parse_file(lines)
    print(navigate_desert(instructions, positions))
    print(navigate_desert_lcm(instructions, positions))
