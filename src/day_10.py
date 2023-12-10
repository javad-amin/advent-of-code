import os
from collections import defaultdict, deque

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(PROJECT_PATH, "src", "input", "day_10.txt")

DIRECTIONS: dict[str, list] = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
}


def mark_inside_tiles(
    grid: list[list[str]], distances: dict[tuple[int, int], int]
) -> None:
    for i, row in enumerate(grid):
        inside = False
        for j, _ in enumerate(row):
            if (i, j) not in distances:
                grid[i][j] = "I" if inside else "O"
            elif (-1, 0) in DIRECTIONS[grid[i][j]]:
                inside = not inside


def bfs_find_distances(
    start: tuple[int, int], adjacent_pipes: dict[tuple[int, int], list[tuple[int, int]]]
) -> dict[tuple[int, int], int]:
    distance: defaultdict = defaultdict(int)
    queue = deque([start])

    while queue:
        current_cell = queue.popleft()
        for next_cell in adjacent_pipes[current_cell]:
            if next_cell not in distance:
                distance[next_cell] = distance[current_cell] + 1
                queue.append(next_cell)

    return distance


def determine_start_pipe(
    grid: list[list[str]],
    start: tuple[int, int],
    adjacent_pipes: dict[tuple[int, int], list[tuple[int, int]]],
) -> None:
    adjacent_start_pipes = find_adjacent_start_pipes(start, adjacent_pipes)

    for key, value in DIRECTIONS.items():
        if set(value) == set(
            (pipe[0] - start[0], pipe[1] - start[1]) for pipe in adjacent_start_pipes
        ):
            grid[start[0]][start[1]] = key
            break

    adjacent_pipes[start] = adjacent_start_pipes


def find_adjacent_start_pipes(
    starting_pipe: tuple[int, int],
    adjacent_pipes: dict[tuple[int, int], list[tuple[int, int]]],
) -> list[tuple[int, int]]:
    return [pipe for pipe in adjacent_pipes if starting_pipe in adjacent_pipes[pipe]]


def find_adjacent_pipes(
    grid: list[list[str]],
) -> dict[tuple[int, int], list[tuple[int, int]]]:
    adjacency_list = defaultdict(list)

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in DIRECTIONS:
                for dx, dy in DIRECTIONS[cell]:
                    x, y = i + dx, j + dy
                    if (
                        0 <= x < len(grid)
                        and 0 <= y < len(grid[x])
                        and grid[x][y] != "."
                    ):
                        adjacency_list[(i, j)].append((x, y))
    return adjacency_list


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        file_content = f.read()

    grid = [list(line) for line in file_content.splitlines()]

    start = next(
        (i, j)
        for i, row in enumerate(grid)
        for j, cell in enumerate(row)
        if cell == "S"
    )

    adjacent_pipes = find_adjacent_pipes(grid)
    determine_start_pipe(grid, start, adjacent_pipes)

    distances = bfs_find_distances(start, adjacent_pipes)
    print(max(distances.values()))

    mark_inside_tiles(grid, distances)
    print(sum(row.count("I") for row in grid))
