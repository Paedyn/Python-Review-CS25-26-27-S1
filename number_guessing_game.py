# Store a secret number between 1 and 10.
# Ask the player to guess the number.
# Use a while loop to continue until they guess correctly.
# Tell the player whether each incorrect guess is too high or too low.
# Print a congratulatory message when they find the correct answer.
number=""

ask= (int(input("Guess the number:")))
while ask < 6:
    print("Too low! Try again!")
    ask = (int(input("Guess the number:")))

while ask> 6:
    print("Too high!Try again")
    ask = (int(input("Guess the number:")))

else:
    print("You got it right!")