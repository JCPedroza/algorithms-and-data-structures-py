"""
This implementation of Bubble Sort:
  * Is an optimized version of the naive version.
  * Returns early if the list is already sorted or is sorted during the process.
  * Doesn't iterate through the sorted portion of the list unnecessarily.

Time Complexity: Best O(n) | Avg O(n^2) | Worst O(n^2)
Space Complexity: Total O(n) | Aux O(1)
"""


def bubble_sort(nums: list[float]) -> list[float]:
    """Sorts a list of floats, in-place."""
    is_sorted = True

    for loop in range(len(nums) - 1):
        for idx in range(len(nums) - loop - 1):
            if nums[idx] > nums[idx + 1]:
                is_sorted = False
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]

        if is_sorted:  # End early, list is sorted
            break

    return nums


algorithm = bubble_sort
name = "optimized"
