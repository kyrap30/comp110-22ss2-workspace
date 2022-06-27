"""EX02 - One shot wordle."""
__author__ = "730466380"

"""Defining secret word and prompting player for guess."""
secret_word: str = "python"
word_guess: str = input(f"What is your {len(secret_word)}-letter word_guess? ")

"""Making sure the guessed word is the length of the secret word."""
while len(secret_word) != len(word_guess):
    a: str = str(input(f"That was not {len(secret_word)} letters! Try again: "))
    word_guess = a
place: int = 0

"""Assigning names to corresponding box/emoji sequence."""
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
WHITE_BOX: str = "\U00002B1C"
box_sequence: str = ""

"""Creating sequence of box emojis""" 
"""based on if any characters in the guessed word are in the secret word"""
"""and correctness of placement."""
while place < len(word_guess):
    if secret_word[place] == word_guess[place]:
        box_sequence += GREEN_BOX
    else: 
        guessed_char: bool = False
        alt_place: int = 0
        while guessed_char is False and alt_place < len(secret_word):
            if word_guess[place] == secret_word[alt_place]:
                b: bool = True
                guessed_char = b
            alt_place += 1
        if guessed_char is False:
            box_sequence += WHITE_BOX
        if guessed_char is True:
            box_sequence += YELLOW_BOX
    place += 1

"""Printing emoji sequence and final message to player."""
if secret_word != word_guess:
    print(box_sequence)
    print("Not quite. Play again soon!")
else: 
    print(box_sequence)
    print("Woo! You got it")