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


def part_one(data: list[str]) -> int:

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

    total = 0
    for line in data:
        total += check_right(line) + check_left(line)
    total += check_down(data)
    total += check_up(data)
    total += check_right_down(data)
    total += check_right_up(data)
    total += check_left_down(data)
    total += check_left_up(data)

    return total


def part_two(data: list[str]) -> int:

    def check_x_mas(data: list[str], a_row: int, a_col: int):

        right = False
        left = False

        # If the top left is either a M or S
        if data[a_row - 1][a_col - 1] in ("M", "S"):
            # If the top left is a M
            if data[a_row - 1][a_col - 1] == "M":
                # Check that the bottom right is a S
                if data[a_row + 1][a_col + 1] == "S":
                    right = True
                else:
                    return False
            # If the top left is a S
            else:
                # Check that the bottom right is a M
                if data[a_row + 1][a_col + 1] == "M":
                    right = True
                else:
                    return False
        # If the top right is either a M or S
        if data[a_row - 1][a_col + 1] in ("M", "S"):
            # If the top right is a M
            if data[a_row - 1][a_col + 1] == "M":
                # Check that the bottom left is a S
                if data[a_row + 1][a_col - 1] == "S":
                    left = True
                else:
                    return False
            # If the top left is a S
            else:
                # Check that the bottom right is a M
                if data[a_row + 1][a_col - 1] == "M":
                    left = True
                else:
                    return False

        return all([right, left])

    count = 0
    for row in range(1, len(data) - 1):
        for col in range(1, len(data[row]) - 1):
            if data[row][col] == "A":
                count += check_x_mas(data, row, col)

    return count


if __name__ == "__main__":

    data = read_input("04")
    part_one_ans = part_one(data)
    print(part_one_ans)

    part_two_ans = part_two(data)
    print(part_two_ans)
