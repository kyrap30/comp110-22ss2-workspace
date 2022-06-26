__author__ = "730466380"
"""EX02 - One shot wordle."""

WORD: str = "python"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

input: int = 0
box_emoji: str = ""
f: int = 0

word_guess: str = input(f"What is your 6-letter guess? ")

if len(WORD) != len(word_guess):
    word_guess: str = str(input("That was not 6 letters! Try again: "))


while input < len(word_guess):
    if WORD[input] == word_guess[input]:
        print(GREEN_BOX)
    else: 
        typed: bool = False
        while typed is not True and f < len(WORD):
            if WORD[f] == word_guess[typed]:
                typed: bool = True
            f += 1
        if typed is not True:
            print(WHITE_BOX)
        else:
            print(YELLOW_BOX)
    input += 1

if word_guess == "python":
    print("Woo! You got it")
    print(box_emoji)
    exit()
else: 
    print("Not quite. Play again soon!")
    print(box_emoji)
    exit()


