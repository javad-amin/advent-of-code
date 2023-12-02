import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(PROJECT_PATH, "src", "input", "day_01.txt")


def sum_calibration_values(lines: list[str]) -> int:
    digits = [
        "".join(ch for ch in line if ch.isdigit())[:1]
        + "".join(ch for ch in line if ch.isdigit())[-1:]
        for line in lines
    ]
    return sum(int(digit) for digit in digits)


def sum_calibration_values_including_spelled_digits(lines: list[str]) -> int:
    digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    corrected_lines = []
    for line in lines:
        spelled_digits_from_left = [
            (word, digit, index)
            for word, digit in digit_map.items()
            if (index := line.find(word)) != -1
        ]
        spelled_digits_from_right = [
            (word, digit, index)
            for word, digit in digit_map.items()
            if (index := line.rfind(word)) != -1
        ]

        corrected_line_left = line
        if spelled_digits_from_left:
            first_digit = min(spelled_digits_from_left, key=lambda x: x[2])
            corrected_line_left = line.replace(first_digit[0], first_digit[1], 1)

        corrected_line_right = line
        if spelled_digits_from_right:
            last_digit = max(spelled_digits_from_right, key=lambda x: x[2])
            corrected_line_right = line.replace(last_digit[0], last_digit[1], -1)
        corrected_lines.append(f"{corrected_line_left}{corrected_line_right}")

    return sum_calibration_values(corrected_lines)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        lines = f.readlines()
        print(sum_calibration_values(lines))
        print(sum_calibration_values_including_spelled_digits(lines))
