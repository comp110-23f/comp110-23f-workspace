"""EX03 - Structured Wordle!"""

__author__ = "730664874"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(secret_word: str, inputted_char: str) -> bool:
    """Checks if the inputted character is in the secret word."""
    assert len(inputted_char) == 1
    index: int = 0
    while (index < len(secret_word)):
        if (secret_word[index] == inputted_char):
            return True
        index += 1
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """Returns string of emojis depending on how close user_guess is to secret_word."""
    assert len(user_guess) == len(secret_word)
    emojiString: str = ""
    index: int = 0
    while (index < len(user_guess)):
        if (user_guess[index] == secret_word[index]):
            emojiString += GREEN_BOX
        elif (contains_char(secret_word, user_guess[index])):
            emojiString += YELLOW_BOX
        else:
            emojiString += WHITE_BOX
        index += 1
    return emojiString


def input_guess(expected_length: int) -> str:
    """Prompts the user to enter a word of a certain length until they do so."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while (len(user_guess) != expected_length):
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    game_turns: int = 6
    user_turn: int = 0
    expected_length: int = 5
    while (user_turn < game_turns):
        print(f"=== Turn {user_turn + 1}/6 ===")
        user_result: str = emojified(input_guess(expected_length), secret_word)
        print(user_result)
        if (user_result == f"{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}"):
            print(f"You won in {user_turn + 1}/6 turns!")
            return None
        user_turn += 1
    print("X/6 - Sorry, try again tomorrow!")
    return None


if __name__ == "__main__":
    main()