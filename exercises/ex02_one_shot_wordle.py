"""EX02 - One shot wordle."""
__author__ = "730466380"

WORD: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

box_emoji: str = ""

word_guess: str = str(input(f"What is your 6-letter guess? "))
while len(WORD) != len(word_guess):
    word_guess: str = str(input("That was not 6 letters! Try again: "))

place: int = 0

while place < len(word_guess):
    if WORD[place] == word_guess[place]:
        box_emoji += GREEN_BOX

    else: 
        typed: bool = False
        actplace: int = 0

        while typed is not True and actplace < len(WORD):
            if WORD[actplace] == word_guess[typed]:
                typed: bool = True
            actplace += 1

        if typed is not True:
            box_emoji += WHITE_BOX 

        else:
            box_emoji += YELLOW_BOX

    place += 1

if word_guess == "python":
    print("Woo! You got it")
    print(box_emoji)
else: 
    print("Not quite. Play again soon!")
    print(box_emoji)