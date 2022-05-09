def factorial(num: int) -> int:
    match num:
        case 0 | 1:
            return 1
        case _:
            return num * factorial(num - 1)


algorithm = factorial
name = 'pattern matching'
