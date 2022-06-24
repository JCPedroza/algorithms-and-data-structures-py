def vsum(nums: list[float]) -> float:
    """Sum together all the numbers in a list using tail recursion and if.

    :param nums: List of numbers.
    :returns: The sum of the numbers in the list.
    """

    def loop(nums: list[float], total: float = 0.0) -> float:
        if not nums:
            return total

        head, *tail = nums
        return loop(tail, head + total)

    return loop(nums)


algorithm = vsum
name = "tail recursion"
