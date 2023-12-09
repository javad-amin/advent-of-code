import os

PROJECT_PATH: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH: str = os.path.join(PROJECT_PATH, "src", "input", "day_05.txt")


def map_ranges(
    current_ranges: list[tuple[int, int]], range_mappings: list[tuple[int, int, int]]
) -> list[tuple[int, int]]:
    mapped_ranges: list[tuple[int, int]] = []

    for destination, source, size in range_mappings:
        source_end = source + size
        temporary_ranges: list[tuple[int, int]] = []

        while current_ranges:
            start, end = current_ranges.pop()

            before_range = (start, min(end, source))
            intersecting_range = (max(start, source), min(source_end, end))
            after_range = (max(source_end, start), end)

            if before_range[1] > before_range[0]:
                temporary_ranges.append(before_range)

            if intersecting_range[1] > intersecting_range[0]:
                remapped_start = intersecting_range[0] - source + destination
                remapped_end = intersecting_range[1] - source + destination
                mapped_ranges.append((remapped_start, remapped_end))

            if after_range[1] > after_range[0]:
                temporary_ranges.append(after_range)

        current_ranges = temporary_ranges

    return mapped_ranges + current_ranges


def map_value(val: int, range_mappings: list[tuple[int, int, int]]) -> int:
    for destination, source, size in range_mappings:
        if source <= val < source + size:
            return destination + (val - source)
    return val


def map_values(
    values: list[int], range_mappings: list[tuple[int, int, int]]
) -> list[int]:
    return [map_value(val, range_mappings) for val in values]


def parse_mapping_data(lines: list[str]) -> list[tuple[int, int, int]]:
    mapping_data: list[tuple[int, int, int]] = []

    for line in lines:
        destination_start, source_start, length = map(int, line.split())

        mapping_data.append((destination_start, source_start, length))

    return mapping_data


def process_values(lines: list[str]) -> None:
    current_values: list[int] = list(map(int, lines[0].split(":")[1].strip().split()))
    mapping_lines: list[str] = []
    for line in lines[2:]:
        if not line:
            current_values = map_values(
                current_values, parse_mapping_data(mapping_lines)
            )
            mapping_lines = []
        else:
            if "map" not in line:
                mapping_lines.append(line)
    print(int(min(current_values)))


def process_ranges(lines: list[str]) -> None:
    seeds: list[int] = list(map(int, lines[0].split(":")[1].strip().split()))
    current_ranges: list[tuple[int, int]] = [
        (start, start + length) for start, length in zip(seeds[0::2], seeds[1::2])
    ]
    mapping_lines: list[str] = []
    for line in lines[2:]:
        if not line:
            current_ranges = map_ranges(
                current_ranges, parse_mapping_data(mapping_lines)
            )
            mapping_lines = []
        else:
            if "map" not in line:
                mapping_lines.append(line)
    print(min(current_ranges, key=lambda x: x[0])[0])


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        lines: list[str] = [line.strip() for line in f.readlines()]
        lines.append("")  # Add empty line to end of file
    process_values(lines)
    process_ranges(lines)
