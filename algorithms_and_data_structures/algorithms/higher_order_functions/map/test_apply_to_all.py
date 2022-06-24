from . import apply_to_all_comp
from . import apply_to_all_forloop

test_subjects = [apply_to_all_comp, apply_to_all_forloop]


def test_apply_to_all():
    nums = [1, 2, 3, 4]

    def is_odd(num):
        return num % 2 != 0

    for subject in test_subjects:
        assert subject.algorithm(is_odd, []) == []
        assert subject.algorithm(is_odd, [10]) == [False]
        assert subject.algorithm(is_odd, nums) == [True, False, True, False]
