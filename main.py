import random


correct_answer = random.randint(1, 100)

score = 0
previous_guesses = []

too_high_messages = ["Too high! Aim lower!", "Nope, that's too much!", "Oof, try a smaller number!"]
too_low_messages = ["Too low! Go up!", "Not quite! Try something bigger.", "You need a higher number!"]




def set_game_difficulty(difficulty_level):
    if difficulty_level == "easy":
        game(10)
    else:
        game(5)

def game(attempts):
    global score
    global previous_guesses
    previous_guesses = []
    print(f"You have {attempts} attempts to guess the number.")
    while attempts > 0:

        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Sorry what was that? Please enter a valid number.")
            continue

        attempts -= 1

        if guess == correct_answer:
            print(f"You got it! The answer was {correct_answer}.")
            score += 1
            return
        elif guess > correct_answer:
            print(random.choice(too_high_messages))
        elif correct_answer > guess:
            print(random.choice(too_low_messages))

            
        if guess in previous_guesses:
            print("You already guessed that number! Try something else.")
            continue  

        previous_guesses.append(guess)  

        if attempts > 0:
            print("Guess again.")
            print(f"You have {attempts} remaining.")
        else:
            print(f"You've run out of guesses. The correct answer was {correct_answer}")
            return

        if attempts == 7:  
            if correct_answer % 2 == 0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")



while True:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")


    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while difficulty not in ["easy", "hard"]:
        print("Invalid difficulty! Please enter 'easy' or 'hard'.")
        difficulty = input("Choose a difficulty: ").lower()
    set_game_difficulty(difficulty)

    play_again = input("Would you like to play again? (yes/no) ").lower()
    if play_again != 'yes':
        print(f"Your total wins: {score}")
        print("Thanks for playing! Goodbye.")
        break