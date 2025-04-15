import random

words_list = ["apple", "mouse", "mango", "banana", "smile"]

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

# stages = ["0", "1", "2", "3", "4", "5", "6"]

lives = 6

random_word = random.choice(words_list).lower()
print(f"{random_word}")

letter_list = []

for letter in random_word:
    letter_list.append("_")

print(letter_list)

while True:
    guessed_letter = input("Enter a letter: ").lower()

    if guessed_letter in random_word:
        for letter_index in range(len(random_word)):
            if guessed_letter == random_word[letter_index]:
                letter_list[letter_index] = guessed_letter
    else:
        lives -= 1
        print(stages[lives])

    print(letter_list)

    if lives == 0:
        print("You lose ")
        break

    if "_" not in letter_list:
        print("you won")
        break
