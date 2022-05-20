"""This optimization gets rid of the loops completely. To see the details
visit https://projecteuler.net/overview=001 (you need to be logged in and pass
the problem to see the solution optimization spoilers).
"""


def sum_divisible_by(n: int, limit: int) -> int:
    """Computes the sum of all the multiples of n up to the given limit.

    :param n: Multiples of this value will be summed.
    :param limit: Limit of the values to sum (inclusive).
    :return: Sum of all the multiples of n up to the given limit.
    """
    p = limit // n
    return n * (p * (p + 1)) // 2


def mul_of_3_or_5(limit: int) -> int:
    """Computes the sum of all the multiples of 3 or 5 below the given limit,
    using filter and range.

    :param limit: Limit of the values to sum (exclusive).
    :return: Sum of all the multiples of 3 or 5 below the given limit.
    """
    return (
        sum_divisible_by(3, limit - 1) +
        sum_divisible_by(5, limit - 1) -
        sum_divisible_by(15, limit - 1)
    )


solution = mul_of_3_or_5
name = 'analytic optimization'
