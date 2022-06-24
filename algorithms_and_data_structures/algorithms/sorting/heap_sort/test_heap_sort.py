from . import heap_sort

test_subjects = [heap_sort]


def test_heap_sort(test_sorting_algorithm):
    test_sorting_algorithm(test_subjects)
