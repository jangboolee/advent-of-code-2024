from pathlib import Path
from math import floor


def read_input(subfolder: str) -> tuple[list[tuple], list[tuple]]:
    """Read in the input of corrupted memory

    Args:
        subfolder (str): Subfolder containing the input file

    Returns:
        str: Corrupted memory file
    """

    file_path = Path(".") / subfolder / "input.txt"
    with open(file_path, "r") as f:
        lines = [line.rstrip() for line in f.readlines()]

    rules = []
    updates = []

    # Toggle to add item to rules or update
    add_rule = True
    for line in lines:
        # Find and skip empty line, and switch toggle
        if line == "":
            add_rule = False
            continue
        # Add rules as a tuple
        if add_rule:
            rules.append(tuple([int(item) for item in line.split("|")]))
        # Add updates as a tuple
        else:
            updates.append(tuple([int(item) for item in line.split(",")]))

    return rules, updates


def check_update_item(item: int, update: tuple, rules: list[tuple]) -> bool:

    # Get the other items before and after the given item in the update
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


def find_correct_updates(
    rules: list[tuple], updates: list[tuple]
) -> list[tuple]:

    correct_updates = []
    for update in updates:
        update_check_results = []
        # Check each item's validity in each update
        for item in update:
            update_check_results.append(check_update_item(item, update, rules))
        # Save update only if all items are valid
        if all(update_check_results):
            correct_updates.append(update)

    return correct_updates


def find_wrong_updates(
    all_updates: list[tuple], correct_updates: list[tuple]
) -> list[tuple]:

    return [update for update in all_updates if update not in correct_updates]


def sum_middle_pgs(updates: list[tuple]) -> int:

    total = 0
    for update in updates:

        mid_i = floor(len(update) / 2)
        total += update[mid_i]

    return total


if __name__ == "__main__":

    rules, updates = read_input("05")
    correct_updates = find_correct_updates(rules, updates)
    middle_pg_sum = sum_middle_pgs(correct_updates)

    wrong_updates = find_wrong_updates(updates, correct_updates)
    pass
