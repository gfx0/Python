import random
import math
from math import log2
from math import ceil

def play_one_game():
    inputMessage = "Please enter 2 values for range:"

    rangeStart = 0
    rangeEnd = 0
    requestingValidInput = True
    while ( requestingValidInput ):
        try:
            rangeStart, rangeEnd = [int(x) for x in input(inputMessage).split()]
            requestingValidInput = False
        except ValueError:
            print("Please type the numbers with a space.")

    rangeNum = rangeEnd - rangeStart
    #debug#print ( rangeNum )
    if rangeNum <= 1 or rangeStart < 0 or rangeEnd < 0:
        print("The range you is too small or erroneous(range too small?).")
        print("Please write a better range.")
        play_one_game()

    triesLeft = ceil(math.log2(rangeNum))
    #debug#print( "triesLeft: ", triesLeft )

    magicNumber = -1
    for i in range(100):
        magicNumber = random.randrange(rangeStart, rangeEnd);

    #debug#print ( "the magic number: ", magicNumber)
    print ( "\nI have picked a number between", rangeStart,
            "and", rangeEnd,", what's your guess?" )

    #lol pessimistic assumption
    userLostTheGame = True
    for tryNumber in range(triesLeft):
        print("You have", triesLeft - tryNumber, "tries left.\n")
        guess = int(input())
        print()#for dat extra\n
        if ( guess < magicNumber ):
            print("This number is lower than the number I have in mind! Next try?")
        elif ( guess > magicNumber ):
            print("This number is higher than the number I have in mind! Another guess?")
        else:
            userLostTheGame = False
            print("Thaat's right! That was my number!")
            break

    if ( userLostTheGame ):
        print("You ran out of tries, sorry :(\n")

    playAgain = input("Play again? y/n: ")
    if ( playAgain.lower() == 'y' ):
        play_one_game()

def start_game():
    play_one_game()

start_game()
