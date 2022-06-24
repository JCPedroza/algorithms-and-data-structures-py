def fibo_even_sum(limit: int) -> int:
    """Generate even fibonacci numbers <= the given limit, directly
    calculating only even members. (no trial division).

    :param limit: Max value of the output.
    :return: Even fibonacci number.
    """

    def loop(acc, fibo, nxt_fibo):
        if fibo > limit:
            return acc
        return loop(acc + fibo, nxt_fibo, 4 * nxt_fibo + fibo)

    return loop(0, 2, 8)


solution = fibo_even_sum
name = "tail recursion with analytic optimization"
