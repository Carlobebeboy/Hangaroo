def getGuessedWord(secretWord,lettersGuessed):
    
    givenword = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            givenword += letter
        else:
            givenword += '_ '
    return givenword
