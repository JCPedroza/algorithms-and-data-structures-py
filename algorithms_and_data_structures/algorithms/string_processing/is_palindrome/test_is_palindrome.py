from . import is_palindrome

test_subjects = [
    is_palindrome
]

complex_pali = '''Anita. .laVa,
    :; la?
    TINa!'''


def test_is_palindrome():
    for subject in test_subjects:
        assert subject.algorithm('')
        assert subject.algorithm(' ')
        assert subject.algorithm(complex_pali)
        assert not subject.algorithm('Nope')
