import random

print("Hi! Welcome to the Number Guessing Game.\nYou will get 3 chances to guess the number. \nLet's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 3 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low, high)
ch = 3                        # Total allowed chances
gc = 0                        # Guess counter

while gc < ch:
    gc += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break

    elif gc >= ch and guess != num:
        print(f'sorry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')