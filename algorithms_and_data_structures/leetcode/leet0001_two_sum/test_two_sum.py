from . import repo_two_sum

solutions = repo_two_sum.solutions


def test_two_sum():
    for subject in solutions:
        assert subject.solution([8, 3], 11) == (0, 1)
        assert subject.solution([1, 5, 3, 2], 7) == (1, 3)
        assert subject.solution([-3, 4, 7, 9, 1, 8, 2, -2], 15) == (2, 5)
