"""Examples of importing in python."""


from lessons import CQ19_helpers


def main() -> None:
    """Entrypoint of program."""
    print(CQ19_helpers.powerful(2, 4))
    print(f"The answer: {CQ19_helpers.THE_ANSWER}")


if __name__ == "__main__":
    main()