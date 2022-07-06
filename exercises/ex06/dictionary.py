"""Functions that are being tested."""
__author__ = "730466380"

def invert()
    things: dict[str,str] 
    return v:k for k,v in things.items()}


def favorite_color(color_list):
    color_list = list(color_list())
    print(color_list)
    x = max(color_list, key = color_list.count)
    return x


def count(num_list: list[str]) -> dict[str,int]:
    frequency = {}
    for i in num_list:
        if i in frequency.keys():
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency