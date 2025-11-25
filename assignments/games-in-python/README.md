

# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman word-guessing game in Python. Practice string manipulation, loops, conditionals, and random selection while creating an interactive console game.

## 📝 Tasks

### 🛠️ Hangman Game Logic

#### Description
Create a Python program that lets a player guess letters to reveal a hidden word. The game should track guesses, display progress, and end with a win or lose message.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept letter guesses from the user
- Display current progress using underscores for hidden letters (e.g., _ a _ _ m a n)
- Track and display the number of incorrect guesses remaining
- End the game when the word is fully guessed or attempts are exhausted
- Show a win message if the player guesses the word, or a lose message if they run out of attempts

#### Example
```
Word: _ a _ _ m a n
Guesses left: 4
Guessed letters: a, m, n
Enter a letter: g
Word: _ a n g m a n
Guesses left: 4
...existing code...
```
