"""EX02 - One shot wordle."""
__author__ = "730466380"

WORD: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
box_emoji: str = ""
f: int = 0

word_guess: str = str(input(f"What is your {len(WORD)} guess? "))

if len(WORD) != len(word_guess):
    word_guess: str = input("That was not 6 letters! Try again: ")


while i < len(word_guess):
    if WORD[i] == word_guess[i]:
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
    i += 1

if word_guess == "python":
    print("Woo! You got it")
    print(box_emoji)
    exit()
else: 
    print("Not quite. Play again soon!")
    print(box_emoji)
    exit()


