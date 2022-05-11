from . import merge_sort

test_subjects = [
    merge_sort
]


def test_merge_sort(test_sorting_algorithm):
    test_sorting_algorithm(test_subjects)
