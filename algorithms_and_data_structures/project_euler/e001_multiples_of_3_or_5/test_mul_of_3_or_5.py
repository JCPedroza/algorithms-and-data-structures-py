from . import mul_of_3_or_5_filter
from . import mul_of_3_or_5_analytic
from . import mul_of_3_or_5_tail

test_subjects = [
    mul_of_3_or_5_filter,
    mul_of_3_or_5_analytic,
    mul_of_3_or_5_tail
]


def test_mul_of3or5():
    for subject in test_subjects:
        assert subject.solution(-1) == 0
        assert subject.solution(0) == 0
        assert subject.solution(3) == 0
        assert subject.solution(4) == 3
        assert subject.solution(6) == 8
        assert subject.solution(10) == 23
