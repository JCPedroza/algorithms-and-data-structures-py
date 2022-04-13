def insertion_sort(nums: list[float]) -> list[float]:
    """Sorts a list in-place using the insertion sort approach.

    This version performs one comparison and moves one number per
    iteration, an improvement over the naive approach.

    Time complexity: O(n) best O(n^2) worst O(n^2) average.
    Space complexity: O(n) total O(1) auxiliary.

    Args:
        nums: A list of numbers.

    Returns:
        The sorted list.
    """

    for indx in range(1, len(nums)):
        buffer = nums[indx]

        if nums[0] > nums[indx]:
            while indx > 0:
                nums[indx] = nums[indx - 1]
                indx -= 1

            nums[0] = buffer

        else:
            while nums[indx - 1] > buffer:
                nums[indx] = nums[indx - 1]
                indx -= 1

            nums[indx] = buffer

    return nums


algorithm = insertion_sort
name = 'optimized'
