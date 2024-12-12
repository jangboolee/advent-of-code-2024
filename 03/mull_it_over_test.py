# import pytest
import re


def extract_mul_instructions(memory: str) -> list[str]:

    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    return re.findall(pattern, memory)


def test_extract_mul_instructions():

    test_section = (
        r"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+"
        r"mul(32,64]then(mul(11,8)mul(8,5))"
    )
    expected = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]

    assert extract_mul_instructions(test_section) == expected
