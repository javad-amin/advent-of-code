import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(PROJECT_PATH, "src", "input", "day_03.txt")


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        lines = f.readlines()
