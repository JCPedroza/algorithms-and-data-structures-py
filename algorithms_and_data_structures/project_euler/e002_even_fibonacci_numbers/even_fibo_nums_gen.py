from typing import Generator


def fibo_even_gen(limit: int) -> Generator[int, None, None]:
    """Generate even fibonacci numbers <= the given limit, without
    using trial division.

    :param limit: Max value of the output.
    :yield: Even fibonacci number.
    """
    current = 2  # Every third fibonacci number is even
    mid = 3
    last = 5

    while (current <= limit):
        yield current

        current = mid + last
        mid = last + current
        last = current + mid


def fibo_even_sum(limit: int) -> int:
    """Compute the sum of the even fibonacci numbers that are <= limit
    using a while loop with accumulator variable and no trial division
    optimization.

    :param limit: Limit of the fibonacci range to sum.
    :return: Sum of the even fibonacci numbers that are <= limit.
    """
    return sum(fibo_even_gen(limit))


solution = fibo_even_sum
name = 'generator and native sum'
