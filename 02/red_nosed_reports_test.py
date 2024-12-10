import pytest


@pytest.fixture
def sample_data():
    return [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


def test_fixture(sample_data):
    assert sample_data[0] == [7, 6, 4, 2, 1]


def check_deltas(report: list[int]) -> bool:
    """Helper to check if any two adjacent levels differ by at least
    1 and at most 3

    Args:
        report (list[int]): A single report

    Returns:
        bool: True if deltas are within accepted levels, False if not
    """

    return all(
        [
            (
                0 < abs(report[i] - report[i + 1])
                and abs(report[i] - report[i + 1]) <= 3
            )
            for i in range(len(report) - 1)
        ]
    )


@pytest.mark.parametrize(
    "index, expected",
    [
        (0, True),
        (1, False),
        (2, False),
        (3, True),
        (4, False),
        (5, True),
    ],
)
def test_check_deltas(sample_data, index, expected):
    report = sample_data[index]
    assert check_deltas(report) == expected


def check_deltas_dampener(report: list[int]) -> tuple[bool]:
    """Helper to check if any two adjacent levels differ by at least
    1 and at most 3

    Args:
        report (list[int]): A single report

    Returns:
        bool: True if deltas are within accepted levels, False if not
    """

    safe_deltas = sum(
        [
            (
                0 < abs(report[i] - report[i + 1])
                and abs(report[i] - report[i + 1]) <= 3
            )
            for i in range(len(report) - 1)
        ]
    )

    if safe_deltas == len(report) - 1:
        # All deltas are safe, with no use of dampener
        return True, False
    elif safe_deltas == len(report) - 2:
        # All deltas except one is safe, with dampener used
        return True, True
    else:
        # Deltas are not safe, even with dampener
        return False, False
