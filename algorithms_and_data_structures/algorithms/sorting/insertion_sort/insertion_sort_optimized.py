def insertion_sort(nums: list[float]) -> list[float]:
    """Sorts a list in-place using the insertion sort approach.

    This version only performs one comparison and moves one number per
    iteration, an improvement over the naive approach.

    Time complexity: O(n) best O(n^2) worst O(n^2) average.
    Space complexity: O(n) total O(1) auxiliary.

    Args:
        nums: A list of numbers.

    Returns:
        The sorted list.
    """

    for target in range(1, len(nums)):
        swap = target
        temp = nums[swap]

        if nums[0] > nums[swap]:
            while swap > 0:
                nums[swap] = nums[swap - 1]
                swap -= 1

            nums[0] = temp
        else:
            while nums[swap - 1] > temp:
                nums[swap] = nums[swap - 1]
                swap -= 1

            nums[swap] = temp

    return nums


algorithm = insertion_sort
name = 'optimized'
