import pytest


@pytest.fixture
def sample_data():
    return [
        "MXSMXM",
        "XAXXAX",
        "MXSSXS",
    ]


def test_fixture(sample_data):
    assert sample_data[0] == "MXSMXM"


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


def test_check_x_mas(sample_data):

    count = 0
    for row in range(1, len(sample_data) - 1):
        for col in range(1, len(sample_data[row]) - 1):
            if sample_data[row][col] == "A":
                count += check_x_mas(sample_data, row, col)

    assert count == 2
