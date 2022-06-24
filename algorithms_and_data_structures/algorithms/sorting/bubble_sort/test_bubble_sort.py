from . import bubble_sort_naive
from . import bubble_sort_optimized


test_subjects = [bubble_sort_naive, bubble_sort_optimized]


def test_bubble_sort(test_sorting_algorithm):
    test_sorting_algorithm(test_subjects)
