import random

def number_guessing_game():
    print("Welcome to number guessing game!")
    print("I have chosen a number between 1 and 50. Try to guess it!")

    number_to_guess=random.randint(1,50)
    attempts=0

    while True:
        guess= int(input("enter your guess: "))
        attempts+=1

        if guess < number_to_guess:
            print("Too Low ! Try Again")
        elif guess > number_to_guess:
            print("Too High ! Try Again")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

number_guessing_game()