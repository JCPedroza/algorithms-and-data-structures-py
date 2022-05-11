from . import selection_sort

test_subjects = [
    selection_sort
]


def test_selection_sort(test_sorting_algorithm):
    test_sorting_algorithm(test_subjects)
