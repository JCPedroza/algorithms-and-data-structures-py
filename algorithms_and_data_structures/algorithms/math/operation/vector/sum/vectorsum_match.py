def vsum(nums: list[float]) -> float:
    """Sum together all the numbers in a list using recursion and
    pattern matching.

    :param nums: List of numbers.
    :returns: The sum of the numbers in the list.
    """
    match nums:
        case []:
            return 0
        case _:
            [head, *tail] = nums
            return head + vsum(tail)


algorithm = vsum
name = "pattern matching"
