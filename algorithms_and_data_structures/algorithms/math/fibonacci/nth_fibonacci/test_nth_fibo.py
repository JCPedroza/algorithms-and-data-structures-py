from . import nth_fibo_forloop
from . import nth_fibo_match
from . import nth_fibo_tail
from . import nth_fibo_recursive
from . import nth_fibo_memo
from . import nth_fibo_analytic

test_subjects = [
    nth_fibo_forloop,
    nth_fibo_match,
    nth_fibo_tail,
    nth_fibo_recursive,
    nth_fibo_memo,
    nth_fibo_analytic
]


def test_nth_fibo():
    for subject in test_subjects:
        assert subject.algorithm(0) == 0
        assert subject.algorithm(1) == 1
        assert subject.algorithm(2) == 1
        assert subject.algorithm(3) == 2
        assert subject.algorithm(4) == 3
        assert subject.algorithm(5) == 5
        assert subject.algorithm(6) == 8
