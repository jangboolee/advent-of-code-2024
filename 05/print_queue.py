from pathlib import Path


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
    update = []

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
            update.append(tuple([int(item) for item in line.split(",")]))

    return rules, update


if __name__ == "__main__":

    rules, update = read_input("05")
    pass
