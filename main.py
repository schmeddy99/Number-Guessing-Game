import random


correct_answer = random.randint(1, 100)
print(f"The correct_answer is {correct_answer}")


def set_game_difficulty(difficulty_level):
    if difficulty_level == "easy":
        
        game(10)
    else:
        game(5)

def game(attempts):

    print(f"You have {attempts} attempts to guess the number.")
    while attempts > 0:
        guess = int(input("Make a guess: "))
        attempts -= 1

        if guess == correct_answer:
            print(f"You got it! The answer was {correct_answer}.")
            return
        elif guess > correct_answer:
            print("Too high!")
        elif correct_answer > guess:
            print("Too low!")
        else:
            print("Sorry what was that?")
        
        
        if attempts > 0:
            print("Guess again.")
            print(f"You have {attempts} remaining.")
        else:
            print(f"You've run out of guesses. The correct answer was {correct_answer}")
            return



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

set_game_difficulty(difficulty)