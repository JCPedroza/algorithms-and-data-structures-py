from pytest import approx

from . import vectorsum_forloop
from . import vectorsum_native
from . import vectorsum_reduce
from . import vectorsum_match
from . import vectorsum_recursive
from . import vectorsum_tail

test_subjects = [
    vectorsum_forloop,
    vectorsum_native,
    vectorsum_reduce,
    vectorsum_match,
    vectorsum_recursive,
    vectorsum_tail
]


def test_vectorsum():
    for subject in test_subjects:
        assert subject.algorithm([]) == 0

        sum_one = subject.algorithm([3.7, 2.9, -4.72, 10.97, -21.72])
        assert sum_one == approx(-8.87)
