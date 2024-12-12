from pathlib import Path
import re


def read_input(subfolder: str) -> str:
    """Read in the input of corrupted memory

    Args:
        subfolder (str): Subfolder containing the input file

    Returns:
        str: Corrupted memory file
    """

    file_path = Path(".") / subfolder / "input.txt"
    with open(file_path, "r") as f:
        return f.read()


def extract_mul_instructions(memory: str) -> list[str]:
    """Helper to extract all mul() instructions that follow the
    mul(X,Y) format

    Args:
        memory (str): The corrupted memory

    Returns:
        list[str]: All found mul() instructions
    """

    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    return re.findall(pattern, memory)


def execute_mul_instruction(instruction: str) -> int:
    """Helper to parse and execute a single mul(X,Y) instruction

    Args:
        instruction (str): A single mul(X,Y) instruction

    Returns:
        int: The product of X and Y in the mul(X,Y) instruction
    """

    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    match = re.search(pattern, instruction)
    X, Y = int(match.group(1)), int(match.group(2))

    return X * Y


def calculate_all_instructions(instructions: list[str]) -> int:
    """Main function to calculate the sum of all mul(X,Y) instructions

    Args:
        instructions (list[str]): List of all identified mul(X,Y) instructions,
            the output of extract_mul_instructions()

    Returns:
        int: The sum of all mul(X,Y) instructions
    """

    total = 0
    for instruction in instructions:
        total += execute_mul_instruction(instruction)

    return total


if __name__ == "__main__":

    data = read_input("03")
    mul_instructions = extract_mul_instructions(data)
    total_mul = calculate_all_instructions(mul_instructions)
