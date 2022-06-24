def fibo(index: int) -> int:
    """Compute the fibonacci number located at the given index, using
    if conditional structure and recursion.

    :param index: Location of the fibonacci number.
    :return: Fibonacci number located at the given index.
    """
    if index == 0:
        return 0
    if index == 1:
        return 1

    return fibo(index - 1) + fibo(index - 2)


algorithm = fibo
name = "if conditional recursion"
