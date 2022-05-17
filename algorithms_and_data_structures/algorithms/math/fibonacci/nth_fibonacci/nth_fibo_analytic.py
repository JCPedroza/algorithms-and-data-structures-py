from math import sqrt


def fibo(index: int) -> int:
    '''Compute the fibonacci number located at the given index, using
    an analytic approach.

    :param index: Location of the fibonacci number.
    :return: Fibonacci number located at the given index.
    '''
    if index == 0:  # Otherwise fibo(0) evaluates to 1
        return 0

    sqrt5 = sqrt(5)
    p = (1 + sqrt5) / 2
    q = 1 / p

    return int((p ** index + q ** index) / sqrt5 + 0.5)


algorithm = fibo
name = 'analytic'
