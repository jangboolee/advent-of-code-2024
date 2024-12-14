from pathlib import Path


def read_input(subfolder: str) -> str:
    """Read in the input of the word search puzzle

    Args:
        subfolder (str): Subfolder containing the input file

    Returns:
        str: Word search contents
    """

    file_path = Path(".") / subfolder / "input.txt"
    with open(file_path, "r") as f:
        return [line.rstrip() for line in f.readlines()]


def check_horizontal(line: str) -> int:

    count = 0
    for i in range(len(line) - 4):
        snippet = line[i : i + 4]
        if snippet == "XMAS":
            count += 1

    return count


def check_backwards(line: str) -> int:

    reverse = line[::-1]
    return check_horizontal(reverse)


def check_down(data: list[str]) -> int:

    count = 0
    for row in range(len(data) - 4):
        for col in range(len(data[row])):

            snippet = ""

            for i in range(4):
                snippet += data[row + i][col]
            if snippet == "XMAS":
                count += 1


def check_up(data: list[str]) -> int:

    count = 0
    for row in range(len(data) - 1, 4, -1):
        for col in range(len(data[row])):

            snippet = ""

            for i in range(4):
                snippet += data[row - i][col]
            if snippet == "XMAS":
                count += 1


if __name__ == "__main__":

    data = read_input("04")
    first = data[0]
    first_count = check_horizontal(first) + check_backwards(first)

    check_down(data)
    check_up(data)

    pass
