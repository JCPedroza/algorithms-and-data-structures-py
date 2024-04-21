"""
This implementation of Bubble Sort:
  * Is a naive version, can be easily optimized.
  * Doesn't return early if the list is already sorted or is sorted during the process.
  * Iterates through the sorted portion of the list unnecessarily.

Time Complexity: Best O(n^2) | Avg O(n^2) | Worst O(n^2)
Space Complexity: Total O(n) | Aux O(1)
"""


def bubble_sort(nums: list[float]) -> list[float]:
    """Sorts a list of floats, in-place."""
    for _ in range(len(nums)):
        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]

    return nums


algorithm = bubble_sort
name = "naive"
