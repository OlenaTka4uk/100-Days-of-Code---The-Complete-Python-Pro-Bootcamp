import random
from hangman_art import stages
from hangman_art import logo
from word_list import word_list

lives = 6
print(logo)
print("Welcome to Hangman Game!")

choosen_word = random.choice(word_list)

print(choosen_word)

placeholder = ""

for position in range(len(choosen_word)):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You already guessed that letter. Try again.")
        continue

    display = ""

    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in choosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("You lose!")
            print(f"The word was: {choosen_word}")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])

