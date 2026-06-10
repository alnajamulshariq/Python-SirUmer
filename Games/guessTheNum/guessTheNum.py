import random

print("Welcome to Guess the Number game!")
print("=================================")

while True:
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
   
    print("\nI've picked a number between 1 and 100. Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            break
   
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing! Goodbye.")
        break