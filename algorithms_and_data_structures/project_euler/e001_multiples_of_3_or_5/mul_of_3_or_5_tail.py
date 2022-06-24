def multiples_of_3_or_5(limit: int) -> int:
    """Computes the sum of all the multiples of 3 or 5 below the given limit,
    using tail recursion.

    :param limit: Limit of the values to sum (exclusive).
    :return: Sum of all the multiples of 3 or 5 below the given limit.
    """

    def loop(acc, num):
        if num < 1:
            return acc
        if num % 3 == 0 or num % 5 == 0:
            return loop(acc + num, num - 1)
        return loop(acc, num - 1)

    return loop(0, limit - 1)


solution = multiples_of_3_or_5
name = "tail recursion if"
