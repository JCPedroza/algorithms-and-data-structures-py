def fibo(index: int) -> int:
    '''Compute the fibonacci number located at the given index, using a
    for loop.

    :param index: Location of the fibonacci number.
    :return: Fibonacci number located at the given index.
    '''
    cur, nxt = 0, 1
    for _ in range(0, index):
        cur, nxt = nxt, cur + nxt
    return cur


algorithm = fibo
name = 'for loop accumulator'
