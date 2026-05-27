import random
import logo
easyLevelAttempt=10
hardLevelAttempt=5

def setDifficulties(level):
    if level=='easy':
        return easyLevelAttempt
    elif level=='hard':
        return hardLevelAttempt
    else:
        return

def checkAnswer(guessedNumber,answer,attempts):
    if guessedNumber < answer:
        print("your guess is too low")
        return attempts-1
    elif guessedNumber > answer:
        print("your guess is too high")
        return attempts-1
    else:
        print(f" Your guess is right.....The answer was {answer}")  

def game():
    print(logo.logo)
    print("Let me think of anumber between 1 to 50") 
    answer=random.randint(1,50)
    level=input("choose level of difficulties..... Type 'easy' or 'hard' ")   
    attempts=setDifficulties(level)
    if attempts != easyLevelAttempt and attempts != hardLevelAttempt:
        print("younhave enterd wrong difficulty level....play again!!")
        return
    guessedNumber=0
    while guessedNumber!=answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessedNumber=int(input("Guess the number: "))
        attempts=checkAnswer(guessedNumber,answer,attempts)
        if attempts==0:
             print("you are out of guesses...you loose")
             print(f"The correct answer was {answer}")
             return
        elif guessedNumber!=answer:
             print("guess again")

game()






