from functools import reduce
from operator import add


def vsum(nums: list[float]) -> float:
    ''' Sum together all the numbers in a list using reduce and the add
    operator.

    :param nums: List of numbers.
    :returns: The sum of the numbers in the list.
    '''
    return reduce(add, nums, 0.0)


algorithm = vsum
name = 'reduce lambda'
