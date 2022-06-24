def merge(left: list[float], right: list[float]) -> list[float]:
    """Merges two number lists, preserving relative order.

    Time complexity: O(n) for best, worst, average
    Space complexity: O(n) total O(n) auxiliary

    Args:
        left: Ordered list of numbers.
        right: Ordered list of numbers.

    Returns:
        Sorted merge of the two lists of numbers.
    """

    merged = []

    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))

    return [*merged, *left, *right]


def merge_sort(nums: list[float]) -> list[float]:
    """Sorts a list of numbers using the Merge Sort approach.

    Time complexity: O(n log n) for best, worst, average.
    Space complexity: O(n).

    Args:
        nums: List of numbers.

    Returns:
        Sorted list of numbers.
    """

    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    return merge(merge_sort(left), merge_sort(right))


algorithm = merge_sort
name = "simple"
