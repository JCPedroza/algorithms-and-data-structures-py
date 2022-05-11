def selection_sort(nums: list[float]) -> list[float]:
    """Sorts a list in-place using the Selection Sort approach.

    Time complexity: O(n^2) for best, worst, and average.
    Space complexity: total O(n) auxiliary O(1).

    Args:
        nums: A list of numbers.

    Returns:
        The sorted list.
    """

    for pivot in range(0, len(nums) - 1):
        smallest = pivot

        # Find smallest value, then swap it with the pivot
        for target in range(pivot + 1, len(nums)):
            if nums[target] < nums[smallest]:
                smallest = target

        nums[pivot], nums[smallest] = nums[smallest], nums[pivot]

    return nums


algorithm = selection_sort
name = "simple"
