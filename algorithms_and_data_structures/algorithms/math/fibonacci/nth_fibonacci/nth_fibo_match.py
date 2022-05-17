def fibo(index: int) -> int:
    '''Compute the fibonacci number located at the given index, using
    pattern matching and recursion.

    :param index: Location of the fibonacci number.
    :return: Fibonacci number located at the given index.
    '''
    match index:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fibo(index - 1) + fibo(index - 2)


algorithm = fibo
name = 'pattern matching recursion'
