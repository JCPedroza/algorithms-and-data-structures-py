def fibo(index: int) -> int:
    """Compute the fibonacci number located at the given index, using
    recursion with memoized results.

    :param index: Location of the fibonacci number.
    :return: Fibonacci number located at the given index.
    """
    results: dict[int, int] = {0: 0, 1: 1}

    def loop(index: int) -> int:
        if index in results:
            return results[index]

        results[index] = loop(index - 1) + loop(index - 2)
        return results[index]

    return loop(index)


algorithm = fibo
name = "recursion with memoization"
