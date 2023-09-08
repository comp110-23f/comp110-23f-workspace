"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730664874"

typed_word: str = input("Enter a 5-character word: ")
if(len(typed_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
typed_char: str = input("Enter a single character: ")
if(len(typed_char) != 1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + typed_char + " in " + typed_word)
count: int = 0
if(typed_word[0] == typed_char):
    print(typed_char + " found at index " + 0)
    count += 1
if(typed_word[1] == typed_char):
    print(typed_char + " found at index " + 1)
    count += 1
if(typed_word[2] == typed_char):
    print(typed_char + " found at index " + 2)
    count += 1
if(typed_word[3] == typed_char):
    print(typed_char + " found at index " + 3)
    count += 1
if(typed_word[4] == typed_char):
    print(typed_char + " found at index " + 4)
    count += 1
if(count > 0):
    print(count + " instances of " + typed_char + " found in " + typed_word)
else:
    print("No instances of " + typed_char + " found in " + typed_word)