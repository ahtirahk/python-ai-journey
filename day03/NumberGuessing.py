import random

secret_number = random.randint(1, 10)
attempts = 0
print("I have picked a number between 1 and 10.")

# Game loop
while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("High! Try again")
    elif guess < secret_number:
        print("Low! Try again")
    else:
        print(f"Correct! You got it in {attempts} attempts!")
        break