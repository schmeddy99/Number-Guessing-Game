import random

attempts = 0

correct_answer = random.randint(1, 100)
print(f"The correct_answer is {correct_answer}")


def set_game_difficulty(difficulty_level):
    global attempts
    if difficulty_level == "easy":
        attempts = 10
        # easy_game()
    else:
        attempts =  5
        # hard_game()



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

set_game_difficulty(difficulty)