"""EX02 - One shot wordle."""
__author__ = "730466380"

WORD: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
box_emoji: str = ""
found_index: int = 0
found: bool = False

word_guess: str = input("What is your 6-letter guess? ")

if len(word_guess) != 6:
    word_guess: str = input("That was not 6 letters! Try again: ")
else: 
    if word_guess[i] == WORD[i]:
       print(GREEN_BOX)
    
if word_guess == "python":
    print("Woo! You got it")
else: 
    print("Not quite. Play again soon!")
    exit()


