def vsum(nums: list[float]) -> float:
    ''' Sum together all the numbers in a list using for loop.

    :param nums: List of numbers.
    :returns: The sum of the numbers in the list.
    '''
    total_sum = 0.0

    for num in nums:
        total_sum += num

    return total_sum


algorithm = vsum
name = 'for loop'
