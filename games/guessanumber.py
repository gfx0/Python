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
    print ( rangeNum )
    if rangeNum == 1:
        print("The range you gave is too small, there can be only one guess.")
        print("Please write a better range.")
        play_one_game()

    triesLeft = ceil(math.log2(rangeNum))
    print( "triesLeft: ", triesLeft )
    
    print ( "I have picked a number between 0 and 200, what's your guess?" )

    #todo: write the guessing logic

def start_game():
    play_one_game()

start_game()
