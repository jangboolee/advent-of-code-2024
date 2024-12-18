import pytest


@pytest.fixture
def sample_data():
    return (
        [
            (47, 53),
            (97, 13),
            (97, 61),
            (97, 47),
            (75, 29),
            (61, 13),
            (75, 53),
            (29, 13),
            (97, 29),
            (53, 29),
            (61, 53),
            (97, 53),
            (61, 29),
            (47, 13),
            (75, 47),
            (97, 75),
            (47, 61),
            (75, 61),
            (47, 29),
            (75, 13),
            (53, 13),
        ],
        [
            (75, 47, 61, 53, 29),
            (97, 61, 53, 29, 13),
            (75, 29, 13),
            (75, 97, 47, 61, 53),
            (61, 13, 29),
            (97, 13, 75, 29, 47),
        ],
    )


def test_fixture(sample_data):

    assert sample_data[0][0] == (47, 53)
    assert sample_data[1][2] == (75, 29, 13)


def check_update_item(item: int, update: tuple, rules: list[tuple]) -> bool:

    update_before = update[: update.index(item)]
    update_after = update[update.index(item) :]

    valid = True
    for first, second in rules:
        if first == item:
            if second in update_before:
                valid = False
        if second == item:
            if first in update_after:
                valid = False

    return valid


def test_checK_update_item(sample_data):

    rules, updates = sample_data

    first_update = updates[0]
    fourth_update = updates[3]

    assert check_update_item(75, first_update, rules) is True
    assert check_update_item(47, first_update, rules) is True
    assert check_update_item(61, first_update, rules) is True
    assert check_update_item(53, first_update, rules) is True

    assert check_update_item(75, fourth_update, rules) is False
