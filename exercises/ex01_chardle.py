"""EX01 - Chardle - A cute step toward Wordle"""
__author__ = "730466380"


WORD_GUESS: str = (input("Enter a 5-character word: "))
if len(WORD_GUESS) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter_guess: str = (input("Enter a single character: "))
if len(letter_guess) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + letter_guess + " in", WORD_GUESS)


num_of_letters: int = 0

if letter_guess == WORD_GUESS[0]:
    num_of_letters = num_of_letters + 1
    print(letter_guess + " found at index 0")
if letter_guess == WORD_GUESS[1]:
    num_of_letterse = num_of_letters + 1
    print(letter_guess + " found at index 1")
if letter_guess == WORD_GUESS[2]:
    num_of_letters = num_of_letters + 1
    print(letter_guess + " found at index 2")
if letter_guess == WORD_GUESS[3]:
    num_of_letters = num_of_letters + 1
    print(letter_guess + " found at index 3")
if letter_guess == WORD_GUESS[4]:
    num_of_letters = num_of_letters + 1
    print(letter_guess + " found at index 4")


if num_of_letters == 0:
    print("No instances of " + str(letter_guess) + " found in " + WORD_GUESS)
if num_of_letters == 1:
    print(str(num_of_letters) + " instance of " + str(letter_guess) + " found in " + WORD_GUESS)
if num_of_letters > 1:
    print(str(num_of_letters) + " instances of " + str(letter_guess) + " found in " + WORD_GUESS)
