from pathlib import Path
from collections import Counter


def read_input(subfolder: str) -> tuple[list[int]]:

    file_path = Path(".") / subfolder / "input.txt"
    with open(file_path, "r") as f:
        f_content = [line.rstrip().split("   ") for line in f.readlines()]

    first = []
    second = []
    for i in f_content:
        first.append(int(i[0]))
        second.append(int(i[1]))

    return first, second


def calc_total_distance(first: list[int], second: list[int]) -> int:

    # Create sorted versions of the two lists
    first_sorted = sorted(first)
    second_sorted = sorted(second)

    # Find the total difference
    distance = 0
    for i in range(len(first_sorted)):
        distance += abs(first_sorted[i] - second_sorted[i])

    return distance


def calc_similarity_score(first: list[int], second: list[int]):

    # Convert list of IDs to dictionary of count per ID
    first_dict = dict(Counter(first))
    second_dict = dict(Counter(second))

    sim_score = 0
    for first_id in first_dict.keys():
        sim_score += second_dict.get(first_id, 0) * first_id

    return sim_score


if __name__ == "__main__":

    first, second = read_input("01")
    distance = calc_total_distance(first, second)
    sim_score = calc_similarity_score(first, second)
