"""COMP110 Assignment 3: Wordle"""

__author__: str = "730509911"

"""Checks letter by letter if a character is in a word"""


def contains_char(word: str, character: str) -> bool:
    assert len(character) == 1, f"len('{character}') is not 1"
    tested: int = 0
    result: bool = False
    while tested < len(word):
        if word[tested] != character:
            tested = tested + 1
        else:
            result = True
            tested = tested + 1
    return result


"""Letter by letter checks if the letter is in that place or in the word then outputs an emoji accordingly"""


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret), "Guess must be same length as secret"
    letter: int = 0
    result: str = ""
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    WHITE_BOX: str = "\U00002B1C"
    while letter < len(guess):
        if contains_char(secret[letter], guess[letter]):
            result = result + GREEN_BOX
            letter = letter + 1
        elif contains_char(secret, guess[letter]):
            result = result + YELLOW_BOX
            letter = letter + 1
        else:
            result = result + WHITE_BOX
            letter = letter + 1
    return result


"""Asks for a word that is the same length as an input number"""


def input_guess(N: int) -> str:
    word: str = input(f"Enter a {N} character word")
    while len(word) != N:
        word = input(f"That wasn't {N} chars! Try again:")
    return word


"""Combines all the previous functions into the Wordle game"""


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    tries: int = 1
    guess: str = ""
    while tries <= 6 and guess != secret:
        print(f"=== Turn {tries}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {tries}/6 turns!")
        elif tries == 6:
            print("X/6 - Sorry, try again tomorrow!")
            tries = tries + 1
        else:
            tries = tries + 1


if __name__ == "__main__":
    main(secret="codes")
