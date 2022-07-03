"""EX04 - HIGH OR LOW."""
__author__ = "730466380"


from random import randint
"""Global variables are defined here."""
secret_number: int
player: str
points: int = 0
EMOJIS: str = "\U0001F920"
turn_list: list()


def main() -> None:
    """Main game loop."""
    global secret_number
    global points
    greet()
    range_pick()
    guessing()
    loop()


def greet() -> None:
    """Greeting to player."""
    global player
    global EMOJIS
    player = input("What is your name? ")
    print(f"Hi {player}! Welcome to 'High or Low!'")
    print("You will be able to pick a range to guess a number from. You will get feedback as to whether your guess is higher or lower than the secret number.")
    print("The larger the range, the harder the game. GOOD LUCK! ")


def loop():
    """Creates loop for the player."""
    global points
    global player
    print(f"{player}, you have guessed a total of {points} times!")
    print("Would you like to continue to another round?")
    range_pick()
    guessing()


def range_pick() -> str:
    """Player chooses either the range of number to use in the game or to exit."""
    print("Pick a range from the following: ")
    print("a: 1-10")
    print("b: 1-50")
    print("c: 1-100")
    print("d: if you would like to exit the game")
    global secret_number
    ans: str = input("Please choose from the choices above (a,b,c, or d): ")
    if ans == "d":
        exit()
    if ans == "a":
        secret_number = randint(1, 10)
    if ans == "b":
        secret_number = randint(1, 50)
    if ans == "c":
        secret_number = randint(1, 100)
    else:
        ans: str = "Please choose a, b, c, or d: "
    return secret_number


def guessing():
    """Player guesses number within range and gets feedback as to whether the secret number is higher or lower."""
    global secret_number
    global player
    global points
    guess = int(input("Guess a number between your picked range: "))
    while guess != secret_number:
        points += 1
        if guess < secret_number: 
            print(f"{guess} is too low.")
        if guess > secret_number:
            print(f"{guess} is too high.")
        guess = int(input("Type another guess: "))
    print(f"{guess} is CORRECT!! \U0001F920 Congrats {player}! You win after {points} guesses!!")
    loop()


if __name__ == "__main__": 
    main() 