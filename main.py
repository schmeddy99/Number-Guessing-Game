import random

attempts = 0

correct_answer = random.randint(1, 100)
print(f"The correct_answer is {correct_answer}")


def set_game_difficulty(difficulty_level):
    global attempts
    if difficulty_level == "easy":
        attempts = 10
        easy_game()
    else:
        attempts =  5
        # hard_game()

def easy_game():
    print("You have 10 attempts to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == correct_answer:
        print(f"You got it! The answer was {correct_answer}.")
    elif guess > correct_answer:
        print("Too high!")
        print("Guess again.")
        print("You have.")
    elif correct_answer > guess:
        print("Too low!")
        print("Guess again.")
        print("You have.")
    else:
        print("Sorry what was that?")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

set_game_difficulty(difficulty)