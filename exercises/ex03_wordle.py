"""EX03, the full wordle experience!"""
__author__ = "730402747"


def contains_char(answer: str, char: str) -> bool:
    """Returns if the char is in the answer at any point."""
    assert len(char) == 1
    var: int = 0
    while var < len(answer):
        if char == answer[var]:
            return True
        var += 1
    if var == len(answer):
        return False
    else:
        return False


def emojified(guess: str, answer: str) -> str:
    """Returns the associated emoji string for the guess vs the answer."""
    assert len(guess) == len(answer)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    final_box: str = ''
    var: int = 0
    while var < len(answer):
        if guess[var] == answer[var]:
            final_box += GREEN_BOX
            var += 1
        else: 
            if contains_char(answer, guess[var]) is True:
                final_box += YELLOW_BOX
            if contains_char(answer, guess[var]) is False:
                final_box += WHITE_BOX
            var += 1
    return final_box


def input_guess(lenn: int) -> str:
    """Ensured stuff is the right length."""
    guess: str = input("Enter a " + str(lenn) + " character word: ")
    while len(guess) != lenn:
        guess = input("That wasn't " + str(lenn) + " chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    count: int = 1
    guess: str = ""
    while count < len(secret) + 2 and guess != secret:
        print("=== Turn " + str(count) + "/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        count += 1
    if guess == secret:
        print("You won in " + str(count - 1) + "/6 turns!")
    if count == len(secret) + 2:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()