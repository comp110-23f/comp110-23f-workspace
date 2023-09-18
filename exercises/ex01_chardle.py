"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730402747"
word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print('Error: Word must contain 5 characters')
    exit()
char: str = input("Enter a single character: ")
if len(char) != 1:
    print('Error: Character must be a single character.')
    exit()
print("searching for " + char + " in " + word)
ticker: int = 0
if char in word[0]:
    ticker += 1
    print(char + ' found at index 0')
if char in word[1]:
    ticker += 1
    print(char + ' found at index 1')
if char in word[2]:
    ticker += 1
    print(char + ' found at index 2')
if char in word[3]:
    ticker += 1
    print(char + ' found at index 3')
if char in word[4]:
    ticker += 1
    print(char + ' found at index 4')
print(str(ticker) + ' instance of ' + char + ' found in '+ word)
