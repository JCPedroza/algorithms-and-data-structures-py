def insertion_sort(nums: list[float]) -> list[float]:
    """Sorts a list in-place using the insertion sort approach.

    This version does more comparisons and moves more data than necessary, so
    it is sub-optimal.

    Time complexity: O(n) best O(n^2) worst O(n^2) average.
    Space complexity: O(n) total O(1) auxiliary.

    Args:
        nums: A list of numbers.

    Returns.
        The sorted list.
    """

    for target in range(1, len(nums)):
        swap = target

        while swap > 0 and nums[swap - 1] > nums[swap]:
            nums[swap - 1], nums[swap] = nums[swap], nums[swap - 1]
            swap -= 1

    return nums


algorithm = insertion_sort
name = 'naive'
