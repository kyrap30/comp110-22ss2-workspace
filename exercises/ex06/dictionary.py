"""Functions that are being tested."""
__author__ = "730466380"


def invert(things: dict[str, str]) -> dict[str, str]:
    """Inverts keys anmd values of dictionary."""
    inv_things = {}
    for key in things:
        value = things[key]
        if value in inv_things:
            raise KeyError("Already exists.")
        inv_things[value] = key
    return inv_things


def favorite_color(color_dict: dict[str, str]) -> str:
    """Finds most popular color."""
    output = {}
    for key in color_dict:
        if color_dict[key] in output:
            output[color_dict[key]] += 1
        else:
            output[color_dict[key]] = 1
    highest = max(output.values())
    for key in color_dict:
        if output[color_dict[key]] == highest:
            return color_dict[key]


def count(num_list: list[str]) -> dict[str, int]:
    """Finds the word with the highest frequency."""
    frequency = {}
    for i in num_list:
        if i in frequency.keys():
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency