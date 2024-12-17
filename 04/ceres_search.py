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


def check_right(line: str) -> int:

    count = 0
    for i in range(len(line) - 3):
        snippet = line[i : i + 4]
        if snippet == "XMAS":
            count += 1

    return count


def check_left(line: str) -> int:

    reverse = line[::-1]
    return check_right(reverse)


def check_down(data: list[str]) -> int:

    count = 0
    for row in range(len(data) - 3):
        for col in range(len(data[row])):

            snippet = ""
            for i in range(4):
                snippet += data[row + i][col]
            if snippet == "XMAS":
                count += 1

    return count


def check_up(data: list[str]) -> int:

    reverse = data[::-1]
    return check_down(reverse)


def check_right_down(data: list[str]) -> int:

    count = 0
    for row in range(len(data) - 3):
        for col in range(len(data[row]) - 3):

            snippet = ""
            for i in range(4):
                snippet += data[row + i][col + i]
            if snippet == "XMAS":
                count += 1

    return count


def check_right_up(data: list[str]) -> int:

    reverse = data[::-1]
    return check_right_down(reverse)


def check_left_down(data: list[str]) -> int:

    reverse = [row[::-1] for row in data]
    return check_right_down(reverse)


def check_left_up(data: list[str]) -> int:

    reverse = [row[::-1] for row in data][::-1]
    return check_right_down(reverse)


if __name__ == "__main__":

    data = read_input("04")
    total = 0
    for line in data:
        total += check_right(line) + check_left(line)
    total += check_down(data)
    total += check_up(data)
    total += check_right_down(data)
    total += check_right_up(data)
    total += check_left_down(data)
    total += check_left_up(data)

    print(total)
