def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    """Finds the index of two integers in a list where their sum equals the given
    target value.

    Time complexity: O(n²)

    :param nums: List of integers.
    :param target: Value that the pair of integers have to ad up to.
    :raises ValueError: Raise error if no solution is found.
    :returns: A tuple with the index of the pair of integers that add up to target.
    """

    for pivot_id, pivot in enumerate(nums):
        for addend_id, addend in enumerate(nums[pivot_id + 1 :], pivot_id + 1):
            if pivot + addend == target:
                return pivot_id, addend_id

    # If we assume that there's always a solution, this should never be reached
    raise ValueError("Sum not found")


solution = two_sum
name = "naive"
