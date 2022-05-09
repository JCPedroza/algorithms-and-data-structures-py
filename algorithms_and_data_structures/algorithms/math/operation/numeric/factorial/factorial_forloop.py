def factorial(num: int) -> int:
    product = 1

    for mult in range(1, num + 1):
        product *= mult

    return product


algorithm = factorial
name = 'for loop'
