"""Utility Functions."""
__author__ = "730466380"


def only_evens(list1: list[int]) -> list[int]:
    """Takes only evens for new list."""
    list_of_evens: list[int] = []
    for evens in list1:
        if evens % 2 == 0:
            list_of_evens.append(evens)
    return list_of_evens
    

def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Sees if two lists are equal."""
    if first_list == second_list:
        return True
    else:
        return False


def sub(a_list: list[int], a: int, b: int) -> list[int]:
    """Returning values from list based on index range specified."""
    x: int = a
    y: int = b
    if a < 0:
        a = 0
    if b > len(a_list):
        b = len(a_list)
    return a_list[x:y]