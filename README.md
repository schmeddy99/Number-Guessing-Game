# Number Guessing Game 🎲

A simple number guessing game in Python where players try to guess a randomly generated number between 1 and 100. The game provides randomized feedback, hints, and difficulty levels.

## How to Play

    Run the script:

    python game.py

    Choose a difficulty level:
        easy: 10 attempts
        hard: 5 attempts
    Enter your guesses. The game will provide feedback:
        "Too high!" if your guess is above the correct answer
        "Too low!" if your guess is below the correct answer
        A hint (even/odd) appears after a few wrong attempts
    If you guess correctly, you win!
    The game tracks your total wins.
    After each round, you can choose to play again or exit.

## Features

    Two difficulty levels: Easy (10 tries) & Hard (5 tries)
    Randomized feedback for incorrect guesses
    Hint system to help after multiple wrong attempts
    Duplicate guess prevention to avoid repeating numbers
    Score tracking across multiple games
    Replayability with an option to restart after each round
    Input validation to prevent crashes on invalid input

## Example Gameplay

``` Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100

Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts to guess the number.
Make a guess: 50
Too high!
Guess again.
You have 9 attempts remaining.
Make a guess: 25
Too low!
Guess again.
You have 8 attempts remaining.
Hint: The number is odd.
...
You got it! The answer was 37.
Would you like to play again? (yes/no): no
Your total wins: 1
Thanks for playing! Goodbye.
```


## License

This game is open-source and free to use.
