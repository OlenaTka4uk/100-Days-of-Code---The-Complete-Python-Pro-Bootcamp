import random

word_list =["wolf", "cat", "video"]

choosen_word = random.choice(word_list)

print(choosen_word)

placeholder = ""

for position in range(len(choosen_word)):
    placeholder += "_"

print(placeholder)

guess = input("Guess a letter: ").lower()

display = ""

for letter in choosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
