"""EX04 - HIGH OR LOW!"""
__author__ = "730466380"


from random import randint
secret_number = int

def main() -> None:
    global secret_number
    greet()
    range_pick()
    guessing()

def greet() -> None:
    player: str = input("What is your name? ")
    print(f"Hi {player}!\U0001F920 Are you ready to play? ")
    print("The larger the range, the harder the game. GOOD LUCK!")

def range_pick() -> str:
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
        secret_number = randint(1,10)
    if ans == "b":
        secret_number = randint(1,50)
    if ans == "c":
        secret_number = randint(1,100)
    else:
        ans: str = "Please choose a, b, c, or d: "
    return secret_number

def guessing():
    points: int = 0
    guess = int(input("Guess a number between your picked range: "))
    while guess != secret_number:
        points += 1
        if guess < secret_number: 
            print(f"{guess} is too low.")
        if guess > secret_number:
            print(f"{guess} is too high.")
        guess = int(input("Type another guess: "))
    print(f"{guess} is CORRECT!!\U0001F920\U0001F485 You win after {points} guesses!!")


if __name__ == "__main__": 
    main()

