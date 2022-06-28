
"""EX03 - Structured Wordle."""
__author__ = "730466380"


def contains_char(searched_string: str, searched_chr: str) -> bool:
    """Checking if the a character is contained in the string."""
    assert len(searched_chr) == 1
    if searched_chr in searched_string:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Given strings of the same length, compares the characters presence and position to the secret."""
    assert len(guess) == len(secret)
    place: int = 0
    box_sequence: str = ""
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    WHITE_BOX: str = "\U00002B1C"
    while place < len(secret):  
        if contains_char(secret, guess[place]) is False:
            box_sequence += WHITE_BOX
        if contains_char(secret, guess[place]) is True:
            if guess[place] == secret[place]:
                box_sequence += GREEN_BOX
            if guess[place] != secret[place]:
                box_sequence += YELLOW_BOX
        place += 1
    return box_sequence


def input_guess(num: int) -> str:
    """Makes sure the word guessed by the user is the same length as the secret word declared in the code."""
    ans: str = input(f"Enter a {num} character word: ")
    while len(ans) != num:
        ans = input(f"That wasn't {num} chars! Try again: ")
    return ans


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn_num: int = 1
    guess: str = ""
    win: bool = False
    while turn_num <= 6 and not win: 
        print(f"===Turn {turn_num}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess != secret:
            turn_num += 1
        if guess == secret:
            win = True
            print(f"You won in {turn_num}/6 turns!")
            turn_num += 1  
    if not win:
        print("X/6 - Sorry, try again tomorrow!")
        

if __name__ == "__main__":
    main()