def mul_of_3_or_5(limit: int) -> int:
    """Computes the sum of all the multiples of 3 or 5 below the given limit,
    using filter and range.

    :param limit: Limit of the values to sum (exclusive).
    :return: Sum of all the multiples of 3 or 5 below the given limit.
    """
    return sum(filter(
        lambda x: x % 3 == 0 or x % 5 == 0,
        range(3, limit)))


solution = mul_of_3_or_5
name = 'filter'
