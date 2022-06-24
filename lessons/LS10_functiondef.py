"""An example function definition."""


def my_max(a:int, b: int) -> int:
# ^ signature line/ "contract"
# name of function is my_max
    """Returns the largest argument."""
    # ^ doc string, describes how to use it
    if a >= b:
        return a
    else:
        return b
    # (if else) is a body block
print(my_max(10 + 1, 10))
result: int = my_max(-50,100)
print(result)