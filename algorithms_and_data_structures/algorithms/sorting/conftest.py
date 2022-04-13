import pytest


@pytest.fixture()
def test_sorting_algorithm():
    def run_tests(test_subjects):
        for subject in test_subjects:
            assert subject.algorithm([]) == []
            assert subject.algorithm([1]) == [1]
            assert subject.algorithm([1, 0, -1, -2]) == [-2, -1, 0, 1]
            assert subject.algorithm([4.1, -8.4, 0.8]) == [-8.4, 0.8, 4.1]

    return run_tests
