from typing import Generator


def fibo_even_gen(limit: int) -> Generator[int, None, None]:
    """Generate even fibonacci numbers <= the given limit.

    :param limit: Max value of the output.
    :yield: Even fibonacci number.
    """
    fibo_current = 2
    fibo_next = 3

    while (fibo_current <= limit):
        yield fibo_current
        fibo_current, fibo_next = fibo_next, fibo_current + fibo_next

        while (fibo_current % 2 != 0):
            fibo_current, fibo_next = fibo_next, fibo_current + fibo_next


def fibo_even_sum(limit: int) -> int:
    """Compute the sum of the even fibonacci numbers that are <= limit
    using a while loop with accumulator variable.

    :param limit: Limit of the fibonacci range to sum.
    :return: Sum of the even fibonacci numbers that are <= limit.
    """
    return sum(fibo_even_gen(limit))


solution = fibo_even_sum
name = 'generator and native sum '
