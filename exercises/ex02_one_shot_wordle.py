"""EX02 - One shot wordle."""
__author__ = "730466380"

WORD: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
actplace: int = 0
place: int = 0
box_emoji: str = ""

word_guess: str = str(input(f"What is your {len(WORD)} guess? "))

while len(WORD) != len(word_guess):
    word_guess: str = str(input("That was not 6 letters! Try again: "))


while place < len(word_guess):

    if WORD[place] == word_guess[place]:
        print(GREEN_BOX)
    else: 
        typed: bool = False

        while typed is not True and actplace < len(WORD):
            if WORD[actplace] == word_guess[typed]:
                typed: bool = True
            actplace += 1

        if typed is not True:
            print(WHITE_BOX)
        else:
            print(YELLOW_BOX)

    place += 1

if word_guess == "python":
    print("Woo! You got it")
    print(box_emoji)
    exit()
else: 
    print("Not quite. Play again soon!")
    print(box_emoji)
    exit()


