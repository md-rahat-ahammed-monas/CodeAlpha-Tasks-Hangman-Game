# CodeAlpha_Hangman-Game

A simple Hangman game developed using Python as part of a Python programming practice/project.

## Project Overview

This project is a simple command-line Hangman game where the player has to guess a randomly selected word one letter at a time.

The player gets a maximum of **6 incorrect guesses** to guess the hidden word correctly.

## Features

* Random word selection
* One-letter-at-a-time guessing
* Maximum 6 incorrect guesses
* Input validation
* Prevents duplicate guesses
* Displays correctly guessed letters
* Shows incorrect guess count
* Win and Game Over conditions
* User-friendly command-line interface

## Concepts Used

* Python Programming
* `random` module
* Lists
* Variables
* `while` loop
* `for` loop
* `if-else` condition
* `input()` for user input
* `print()` for displaying output
* String manipulation
* `isalpha()` for input validation
* `all()` function
* List `append()` method

## How the Program Works

1. The program stores a list of words.
2. The `random.choice()` function randomly selects one word.
3. The selected word remains hidden from the player.
4. The player guesses one letter at a time.
5. Correctly guessed letters are displayed.
6. Incorrect guesses increase the incorrect guess counter.
7. The player can make a maximum of **6 incorrect guesses**.
8. If all letters are guessed correctly, the player wins.
9. If the player reaches 6 incorrect guesses, the game ends.
10. The hidden word is displayed at the end of the game.

## Example

```text
Here We Go!
Welcome to the Game of Hangman
Guess the word one letter at a time!
Keep in mind that you have only 6 incorrect guesses.

Word: _ _ _ _ _ _ _

Guess a letter: g
✓ Correct guess!

Word: g _ _ _ _ _ _

Guess a letter: a
✗ Wrong guess!
Incorrect guesses: 1 / 6
```

### Winning Example

```text
Word: g r a v i t y

Congratulations! You won!
The word was: gravity
```

### Game Over Example

```text
✗ Wrong guess!
Incorrect guesses: 6 / 6

💀 Game Over!
The word was: friction
```

## Word List

The game currently contains the following words:

* `force`
* `gravity`
* `inertia`
* `friction`
* `motion`

## Technology Used

**Language:** Python

**Development Environment:** Visual Studio Code

**Python Module:** `random`

## Project Structure

```text
CodeAlpha_Hangman-Game/
│
├── hangman.py
└── README.md
```

## Learning Outcomes

Through this project, I practiced:

* Python fundamentals
* Loops and conditional statements
* Lists and strings
* User input validation
* Random selection
* Basic game logic
* Problem-solving and debugging

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/CodeAlpha_Hangman-Game.git
```

### 2. Open the project folder

```bash
cd CodeAlpha_Hangman-Game
```

### 3. Run the Python program

```bash
python hangman.py
```

## Project Goal

The goal of this project is to practice fundamental Python programming concepts by developing a simple interactive command-line game.





