from . import mul_of3or5_naive

test_subjects = [
    mul_of3or5_naive
]


def test_mul_of3or5():
    for subject in test_subjects:
        assert subject.solution(10) == 23
