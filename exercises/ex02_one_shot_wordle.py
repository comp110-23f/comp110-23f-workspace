"""EX02 - One-Shot Wordle: Loops!"""

__author__ = "730664874"

secret_word: str = "python"
user_guess: str = input("What is your 6-letter guess? ")
curr_index: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
checked_guess: str = ""

while (len(user_guess) != len(secret_word)):
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
while (curr_index < len(secret_word)):
    if (user_guess[curr_index] == secret_word[curr_index]):
        checked_guess += GREEN_BOX
    else:
        search_index: int = 0
        index_found: int = 0
        while (search_index < len(secret_word)):
            if (user_guess[curr_index] == secret_word[search_index]):
                index_found += 1
            search_index += 1
        if (index_found > 0):
            checked_guess += YELLOW_BOX
            print(user_guess[index_found])
        else:
            checked_guess += WHITE_BOX
    curr_index += 1
print(checked_guess)
if (user_guess == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")