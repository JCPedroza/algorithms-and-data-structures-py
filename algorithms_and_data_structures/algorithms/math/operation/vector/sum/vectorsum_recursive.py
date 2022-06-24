def vsum(nums: list[float]) -> float:
    """Sum together all the numbers in a list using recursion and if.

    :param nums: List of numbers.
    :returns: The sum of the numbers in the list.
    """
    if not nums:
        return 0

    head, *tail = nums
    return head + vsum(tail)


algorithm = vsum
name = "recursive"
