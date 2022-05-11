def heapify(nums: list[float], size: int, root: int) -> None:
    """Converts subtree into max heap, and recursively operates on
    affected subtrees.

    Time complexity: best O(1) worst O(log n) average O(log n)?
    Space complexity: total O(n)? auxiliary O(log n)? depth of recursion tree?

    Args:
        nums: List of numbers.
        size: Size of heap.
        root: Index of root node.
    """

    left = root * 2 + 1
    right = left + 1
    largest = root

    if left < size and nums[left] > nums[largest]:
        largest = left
    if right < size and nums[right] > nums[largest]:
        largest = right

    if root != largest:
        nums[root], nums[largest] = nums[largest], nums[root]
        heapify(nums, size, largest)


def heap_sort(nums: list[float]) -> list[float]:
    """Sorts list of numbers in-place, using the Heap Sort approach.

    Time complexity: O(n log n) for best, worst, average.
    Space complexity: total O(n) auxiliary O(1).

    Args:
        nums: List of numbers.

    Returns:
        Sorted list of numbers.
    """

    # Convert list into heap
    for index in range(len(nums) // 2 - 1, -1, -1):
        heapify(nums, len(nums), index)

    # Extract root node (max value) from heap, until heap is empty
    for index in range(len(nums) - 1, -1, -1):
        nums[0], nums[index] = nums[index], nums[0]
        heapify(nums, index, 0)

    return nums


algorithm = heap_sort
name = "simple"
