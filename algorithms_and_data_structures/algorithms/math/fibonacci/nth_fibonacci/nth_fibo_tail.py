def fibo(index: int) -> int:
    '''Compute the fibonacci number located at the given index, using
    pattern matching and tail recursion.

    :param index: Location of the fibonacci number.
    :return: Fibonacci number located at the given index.
    '''
    def loop(cur: int, nxt: int, index: int) -> int:
        match index:
            case 0:
                return cur
            case _:
                return loop(nxt, cur + nxt, index - 1)

    return loop(0, 1, index)


algorithm = fibo
name = 'pattern matching tail racursion'
