import random

words = ["force", "gravity", "inertia", "friction", "motion"]

word = random.choice(words)

guessed_letters = []

incorrect_guesses = 0
max_guesses = 6

print("Here We Go!")
print("Welcome to the Game of Hangman")
print("Guess the word one letter at a time!")
print("Keep in mind that you have only 6 incorrect guesses.")

while incorrect_guesses < max_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        print("The word was:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✓ Correct guess!")
    else:
        incorrect_guesses += 1
        print("✗ Wrong guess!")
        print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

if incorrect_guesses == max_guesses:
    print("\n💀 Game Over!")
    print("The word was:", word)
