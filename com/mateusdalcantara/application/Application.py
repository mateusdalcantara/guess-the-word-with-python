from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0


def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print(f"Too high. You got {turns} left")
        return turns - 1
    elif user_guess < actual_answer:
        print(f"Too low You. got {turns} left")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


def set_dificulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psst, the correct answer is {answer}")

    turns = set_dificulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    while guess != answer:
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == -1:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
