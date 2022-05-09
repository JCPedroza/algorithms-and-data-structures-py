def factorial(num: int) -> int:
    def loop(num: int, prod: int = 1):
        return prod if num < 2 else loop(num - 1, num * prod)

    return loop(num)


algorithm = factorial
name = 'tail recursion'
