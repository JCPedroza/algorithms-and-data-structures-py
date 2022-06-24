from typing import Callable


def apply_to_all(fun: Callable, lst: list) -> list:
    """Apply function to all elements in list, and return a list with the results.

    :param fun: Function to be applied.
    :param lst: Elements of this list will be fed as arguments to the function.
    :return: New list containing the results of applyng the function to every element
    in the list.
    """
    results = []

    for item in lst:
        results.append(fun(item))

    return results


algorithm = apply_to_all
name = "for loop accumulator"
