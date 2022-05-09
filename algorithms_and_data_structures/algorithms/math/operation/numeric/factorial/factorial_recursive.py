def factorial(num: int) -> int:
    if num < 2:
        return 1

    return num * factorial(num - 1)


algorithm = factorial
name = 'recursive if'
