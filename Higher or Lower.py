# starting the loop for the game

import random
play = "Yes"
while  play == "Yes" or play == "yes":

# setup/reset for the game

    num_max = 0
    secret_number = 0
    guess = 0
    attempts = 1

    print("Pick any whole number higher then 1 to set the maximum number for the higher or lower game.,")

# letting the user pick the number and making sure it is an integer higher than 1

    while num_max == 0:
        try:
            num_max = int(input("what do you want as maximum number?: "))

            if num_max <= 1:
                    print("Please enter a whole number/integer higher then 1.")

        except ValueError:
            print("Please enter a whole number/integer higher then 1.")

# creating the number that the user needs to guess

    secret_number = random.randint(1, num_max)
    print(f"The number is between 1 and {num_max}.")

# a loop to make sure the user put in a number and that it

    while guess == 0:
        try:
            guess = int(input("Enter your guess, you will be told that the secret number higher or lower is then your guess: "))

            if guess < 1:
                print("Please enter a whole number/integer higher then 1")

        except ValueError:
            print(f"Please enter a whole number/integer higher that is between 1 and {num_max} ")

# a loop to check if the user put in a number and tels the user if the answer is higher or lower

    while guess != secret_number:
        try:
            if guess < secret_number:
                guess = int(input("Higher, enter a new guess: "))
                attempts = attempts + 1

            if guess > secret_number:
                guess = int(input("Lower, enter a new guess: "))
                attempts = attempts + 1

        except ValueError:
            print("Please enter a whole number/integer higher then 1")

# after the correct number is guessed tel the user the number and how manny attempt it took

    print(f"You got the number right it was {secret_number} goodjob! you did it in {attempts} attempts.")

# ask the user if they want to play again and then restarting the program or exiting it

    play = input("Do you want to play again? type Yes if you do: ")

    if play  == "Yes" or play == "yes":
            print("Restarting game.")

    else:
        print("Thank you for playing.")
        print("Closing game")
        raise SystemExit