def fibo_even_sum(limit: int) -> int:
    """Compute the sum of the even fibonacci numbers that are <= limit
    using a while loop with accumulator and trial division.

    :param limit: Max value of the fibonacci range to sum.
    :return: Sum of the even fibonacci numbers that are <= limit.
    """
    even_sum = 0
    fibo_current = 0
    fibo_next = 1

    while (fibo_current <= limit):
        if (fibo_current % 2 == 0):
            even_sum += fibo_current

        fibo_current, fibo_next = fibo_next, fibo_current + fibo_next

    return even_sum


solution = fibo_even_sum
name = 'while loop with accumulator'
