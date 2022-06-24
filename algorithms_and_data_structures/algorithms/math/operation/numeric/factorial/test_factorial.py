from . import factorial_forloop
from . import factorial_native
from . import factorial_recursive
from . import factorial_reduce
from . import factorial_match
from . import factorial_tail

test_subjects = [
    factorial_forloop,
    factorial_native,
    factorial_recursive,
    factorial_reduce,
    factorial_match,
    factorial_tail,
]


def test_factorial():
    for subject in test_subjects:
        assert subject.algorithm(0) == 1
        assert subject.algorithm(1) == 1
        assert subject.algorithm(2) == 2
        assert subject.algorithm(3) == 6
        assert subject.algorithm(4) == 24
        assert subject.algorithm(5) == 120
