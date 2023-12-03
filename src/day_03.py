import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(PROJECT_PATH, "src", "input", "day_03.txt")

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def find_number_and_y_indices(line, y):
    def expand_in_direction(start, step):
        part_number = ""
        indices = []
        while 0 <= start < len(line) and line[start].isdigit():
            part_number += line[start]
            indices.append(start)
            start += step
        return part_number, indices

    left_part_number, left_indices = expand_in_direction(y, -1)
    right_part_number, right_indices = expand_in_direction(y + 1, 1)

    part_number = left_part_number[::-1] + right_part_number
    y_indices = left_indices[::-1] + right_indices

    return part_number, y_indices


def is_out_of_bound(grid: list[list[str]], x: int, y: int) -> bool:
    return not (0 <= x < len(grid) and 0 <= y < len(grid[0]))


def find_adjacent_numbers(
    grid: list[list[str]],
    current_row: int,
    current_column: int,
    found_number_indices: set[tuple[int, int]],
):
    adjacent_numbers = []
    for row_offset, column_offset in DIRECTIONS:
        new_row, new_column = current_row + row_offset, current_column + column_offset
        if (
            is_out_of_bound(grid, new_row, new_column)
            or not grid[new_row][new_column].isdigit()
            or (new_row, new_column) in found_number_indices
        ):
            continue
        number, line_indices = find_number_and_y_indices(grid[new_row], new_column)
        found_number_indices.update(
            (new_row, line_index) for line_index in line_indices
        )
        if number:
            adjacent_numbers.append(number)
    return adjacent_numbers


def sum_adjacent_gear_ratios(grid: list[list[str]]) -> int:
    total_ratio = 0
    found_number_indices: set[tuple[int, int]] = set()
    for current_row in range(len(grid)):
        for current_column in range(len(grid[0])):
            if grid[current_row][current_column] == "*":
                adjacent_numbers = find_adjacent_numbers(
                    grid, current_row, current_column, found_number_indices
                )
                if len(adjacent_numbers) == 2:
                    total_ratio += int(adjacent_numbers[0]) * int(adjacent_numbers[1])
    return total_ratio


def is_symbol(grid: list[list[str]], x: int, y: int) -> bool:
    return not grid[x][y].isdigit() and grid[x][y] != "."


def sum_adjacent_numbers(grid: list[list[str]]) -> int:
    total_sum = 0
    found_number_indices: set[tuple[int, int]] = set()
    for current_row in range(len(grid)):
        for current_column in range(len(grid[0])):
            if is_symbol(grid, current_row, current_column):
                adjacent_numbers = find_adjacent_numbers(
                    grid, current_row, current_column, found_number_indices
                )
                total_sum += sum(int(number) for number in adjacent_numbers)
    return total_sum


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        schematic = [list(line.strip()) for line in f.readlines()]
    print(sum_adjacent_numbers(schematic))
    print(sum_adjacent_gear_ratios(schematic))
