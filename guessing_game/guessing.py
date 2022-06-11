import random

guessesTakenMe = 0
guessesTakenComputer = 0

maxTries = 20
upperBound = 40

computer_guess = upperBound/2

currentLow = 0
currentHigh = upperBound

playerWins = False
computerWins = False

number = random.randint(1, int(upperBound))
print(f"Guess a number between 1 and {int(upperBound)}\nYou have {int(maxTries)} tries left")

while guessesTakenMe < maxTries:
    guess = int(input("Make a guess\n"))
    guessesTakenMe += 1

    if guess < number:
        print(f" Your guess of {guess} is too Low")
    elif guess > number:
        print(f" Your guess of {guess} is too High")
    else:
        playerWins = True
        break


    computer_guess = int(computer_guess)
    print(f" Computer AI: {str(computer_guess)}")

    if computer_guess < number:
        print(f"Computer guess of {str(computer_guess)} is too Low")
        currentLow = max(currentLow, computer_guess)
        computer_guess = (currentHigh + currentLow)/2
    elif computer_guess > number:
        print(f"Computer guess of {str(computer_guess)} is too High")
        currentHigh = max(currentHigh, computer_guess)
        computer_guess = (currentHigh + currentLow)/2
    else:
        computerWins = True
        break

if playerWins:
    print(f" Good Job player! The correct number was {number}. \n You guessed it in {str(guessesTakenMe)} guesses")
    print(f" Sorry the Computer,  You lose. computer guesses {computer_guess}")

elif computerWins:
    print(f" The computer Wins! The correct number was {number}  in {str(guessesTakenMe)} guesses")
    print(f"Sorry you Player , You Lose. Your guess was {guess} and guess taken was {str(guessesTakenMe)}")
else:
    print(f"Sorry, You've had too many guesses. The number I was thinking of was {str(number)}")











    

