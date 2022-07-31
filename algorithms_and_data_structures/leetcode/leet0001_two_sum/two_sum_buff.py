from typing import Dict


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    """Finds the index of two integers in a list where their sum equals the given
    target value.

    Time complexity: O(n)

    :param nums: List of integers.
    :param target: Value that the pair of integers have to ad up to.
    :raises ValueError: Raise error if no solution is found.
    :returns: A tuple with the index of the pair of integers that add up to target.
    """

    buffer: Dict[int, int] = {}

    for idx, num in enumerate(nums):
        diff = target - num
        if diff in buffer:
            return buffer[diff], idx
        buffer[num] = idx

    # If we assume that there's always a solution, this should never be reached
    raise ValueError("Sum not found")


solution = two_sum
name = "naive"
