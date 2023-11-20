"""EX02, wordle where the player gets one chance to guess the correct word."""
__author__ = "730402747"

word: str = 'python'
guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
final_box: str = ''
while len(guess) != len(word):
    guess = input("That was not 6 letters! Try again: ")
if len(guess) == len(word):
    var: int = 0
    while var < len(word):
        if guess[var] == word[var]:
            final_box += GREEN_BOX
        else: 
            check: int = 0
            same: bool = False
            while check < len(word):
                if guess[var] == word[check]:
                    same = True
                check += 1
            if same is True:
                final_box += YELLOW_BOX
            if same is False:
                final_box += WHITE_BOX
        var += 1
    print(final_box)
    if guess == word:
        print('Woo! You got it!')
    else:
        print('Not quite. Play again soon!')
