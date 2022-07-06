"""Utility Functions."""
__author__ = "730466380"


def only_evens(list1: list[int]) -> list[int]:
    """Takes only evens for new list."""
    list_of_evens: list[int] = list()
    for i in list1:
        if i % 2 == 0:
            list_of_evens.append(list1[i])
            i = i + 1
            return list_of_evens


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Sees if two lists are equal."""
    if first_list == second_list:
        return True
    else:
        return False


def sub (a_list: list[int], a: int, b: int):
    """Returning values from list based on index range specified."""
    if a < 0:
        a = 0
        return a
    if b > len(a_list):
        b = len(a_list)
        return b
    return a_list[a:b]