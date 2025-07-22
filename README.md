# Guess-the-number_Game
**Objective**
The objective of this project is to build a simple number guessing game that challenges the user to identify a randomly selected number within a specified range. The game begins by allowing the user to define a range by entering a lower and an upper bound (for example, from A to B). Once the range is set, the system randomly selects an integer that falls within this user-defined interval. The user's task is then to guess the chosen number using as few attempts as possible. The game provides feedback after each guess, helping the user refine their next guess based on whether their previous attempt was too high or too low.

**How the Game Works**
To understand how the number guessing game functions, let’s walk through two practical scenarios. These examples demonstrate how narrowing down the range intelligently—similar to a binary search—can help guess the number efficiently.

Example 1: Guessing in a Range from -1 to 100
Suppose the user defines the range from -1 to 100, and the system randomly selects 42 as the target number. The guessing process might look like this:

Guess 1: 20 → Too low! Try a higher number.
Guess 2: 80 → Too high! Try a lower number.
Guess 3: 76 → sorry! The number was 59. Better luck next time.
Total Guesses: 3

Example 2: Guessing in a Range from 1 to 20
Now consider a smaller range, from 1 to 50, with the same target number 42. Here's how the guesses might proceed:

Guess 1: 1 → Too low! Try a higher number.
Guess 2: 5 → Correct! The number is 5. You guessed it in 2 attempts.
Total Guesses: 2

**Algorithm**
Accept lower and upper bounds from the user.
Generate a random number in the selected range.
Calculate the maximum allowed guesses using the binary search formula.
Run a loop to take user guesses:
If the guess is too high, print: "Try Again! You guessed too high."
If the guess is too low, print: "Try Again! You guessed too small."
If the guess is correct, print: "Congratulations!" and exit the loop.
If the user runs out of chances, display the correct number and a message: "Better Luck Next Time!"

**Output**

<img width="771" height="440" alt="image" src="https://github.com/user-attachments/assets/a06d593d-8ee1-4898-aecc-3d026a26b77a" />

<img width="724" height="373" alt="image" src="https://github.com/user-attachments/assets/4cab887e-40ab-4959-ae08-1a46fc67bbd1" />
