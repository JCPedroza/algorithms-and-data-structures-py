from functools import reduce
from operator import mul


def factorial(num: int) -> int:
    return reduce(mul, range(1, num + 1), 1)


algorithm = factorial
name = 'reduce'
