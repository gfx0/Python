#-------------------------------------------------------------------------------
#
# This is a simple hangman game implementation for Python practice purposes.
#
#-------------------------------------------------------------------------------

g_word_list = ["Obi-Wan KENOBI", "anathema", "claire", "Amanda"]
g_max_tries = 10
g_alphabet_to_use = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

def display_main_menu():
    print ( "" )
    print ( "****************************" )
    print ( "*~~~~~ PYTHON HANGMAN ~~~~~*" )
    print ( "****************************" )
    print ( "" )
    print ( "****************************" )
    print ( "*~~~~~~~~~~~~~~~~~~~~~~~~~~*" )
    print ( "* Please choose an option: *" )
    print ( "*~~ Start a new game (y) ~~*" )
    print ( "*~~~~~~~~ Quit (n) ~~~~~~~~*" )
    print ( "*~~~~~~~~~~~~~~~~~~~~~~~~~~*" )
    print ( "****************************" )
    print ( "" )

def get_one_character_from_user():

    while ( True ):
        print ( "Type your choice: " ) 
        choice = input()
        choiceCharacterAmount = len(choice)
        if choiceCharacterAmount == 1:
            return choice
        elif choiceCharacterAmount <= 0:
            print ( "Please type atleast one character." )
        else:
            print ( "Please only type one character." )        

    return choice

def ask_for_restart_game():
    didPlayerChooseToPlayAgain = False
    validatingInput = True
    while ( validatingInput ):
        choice = get_one_character_from_user()
        if choice.lower() == 'y':
            validatingInput = False
            didPlayerChooseToPlayAgain = True
        if choice.lower() == 'n':
            validatingInput = False
            
    return didPlayerChooseToPlayAgain

def obfuscate(word, lettersGuessed):
    obfuscatedWord = ""
    for letter in word:
        foundMatchingLetter = False
        for guessedLetter in lettersGuessed:
            capsLetter = letter
            capsGuessedLetter = guessedLetter
            if capsLetter.upper() == capsGuessedLetter.upper():
                foundMatchingLetter = True
                obfuscatedWord += guessedLetter
                break

        if not foundMatchingLetter:
            hasSpecialCharacter = True
            for alphabetLetter in str(g_alphabet_to_use):
                capsAlphabetLetter = alphabetLetter
                capsLetter = letter
                if capsAlphabetLetter.upper() == capsLetter.upper():
                    hasSpecialCharacter = False

            #this could be a - or a ? or other special character
            if hasSpecialCharacter:
                obfuscatedWord += letter
            else:
                obfuscatedWord += "_"

    return obfuscatedWord

def play_one_game( wordToGuess, maxTries ):
    currentTries = maxTries
    lettersUsed = str(g_alphabet_to_use)
    lettersGuessed = ""

    while( currentTries > 0 ):

        currentResult = obfuscate( wordToGuess, lettersGuessed )
        if currentResult.upper() == wordToGuess.upper():
            print( "\nCongratulations! You guessed the right word!\n")
            print( "The right word was: ", currentResult )
            return True
            
        print ( currentResult )
        print ( "Letters available: ", lettersUsed )
        print ( "Tries left: ", currentTries )

        
        #Disallow player to use the same letter twice etc.
        validatingUsedLetter = True
        triedSameLetter = False
        while ( validatingUsedLetter ):
            choice = get_one_character_from_user()
            for letter in lettersGuessed:
                if letter.upper() == choice.upper():
                    print( "\nYou already used that letter, please choose another.\n" )
                    triedSameLetter = True
                    break
            if triedSameLetter:
                break
            validatingUsedLetter = False
            lettersGuessed += choice.upper()
            lettersUsed = lettersUsed.replace(choice.upper(), "")

        if not triedSameLetter:
            currentTries -= 1

    return False

def start_game():
    display_main_menu()

    didGameRunOutOfWords = True
    if ask_for_restart_game():
        for word in g_word_list:
            if not play_one_game( word, g_max_tries ):
                #player has failed to guess the correct word
                print ("\nSorry you ran out of tries!\n")
                start_game()
            else:
                print( "Do you want to play again? (y) / (n)" )
                if not ask_for_restart_game():
                    didGameRunOutOfWords = False
                    print("Bye :)")
                    break
        if didGameRunOutOfWords:
            print("Game ran out of words, sorry, good bye!")
    else:
        print("Bye :)")


start_game()
