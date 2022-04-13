from . import insertion_sort_naive
from . import insertion_sort_optimized


test_subjects = [
    insertion_sort_naive,
    insertion_sort_optimized
]


def test_insertion_sort(test_sorting_algorithm):
    test_sorting_algorithm(test_subjects)
