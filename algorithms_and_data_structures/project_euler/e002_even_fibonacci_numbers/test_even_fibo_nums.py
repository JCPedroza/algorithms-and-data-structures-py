from . import even_fibo_nums_while
from . import even_fibo_nums_gen

test_subjects = [
    even_fibo_nums_while,
    even_fibo_nums_gen
]


def test_even_fibo_nums():
    for subject in test_subjects:
        assert subject.solution(-1) == 0
        assert subject.solution(0) == 0
        assert subject.solution(2) == 2
        assert subject.solution(10) == 10
        assert subject.solution(60) == 44
