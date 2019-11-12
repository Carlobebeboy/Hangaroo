def isWordGuessed(secretWord,lettersGuessed):
           
    for letter in secretWord:
        if letter in lettersGuessed:
            return ("true")
        else:
            return ("false")
        
def getGuessedWord(secretWord,lettersGuessed):
    
    givenword = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            givenword += letter
        else:
            givenword += '_ '
    return givenword

def getAvailableLetters(lettersGuessed):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for letter in lettersGuessed:
        alphabet.remove(letter)
        
        return ' '.join(alphabet)
    
secretWord = "rambutan"    

def hangaroo(secretWord):
    
    intro = str(len(secretWord))
    mistakesMade = 8
    guess = str
    wordGuessed = False
    lettersGuessed = []
        
    print ('Lets start to play, Hangaroo! LEZGAW!!')
    print ("You have to guess a word that is," + intro, "letters long.")
    print ('------------')

    while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False:
         if secretWord == getGuessedWord(secretWord, lettersGuessed):
             wordGuessed = True
             break
         print ('OOPS!!,' + str(mistakesMade), ' guesses left.')
         print ('Available letters: ')
         print(getAvailableLetters(lettersGuessed))
         guess = input('Please guess a letter: ').lower()
         if guess in secretWord:
             if guess in lettersGuessed:
                print ("Oops! You've already guessed that letter: ")
                print (getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
             else:
                lettersGuessed.append(guess)
                print ('Good guess: ') 
                print (getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
         else:
             if guess in lettersGuessed:
                print ("Oops! You've already guessed that letter: ") 
                print (getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
             else:
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print ('Oops! That letter is not in my word: ') 
                print (getGuessedWord(secretWord, lettersGuessed))
                print ('------------')

    if wordGuessed == True:
        return 'Congratulations, you won!'
    elif mistakesMade == 0:
        print ('Sorry, you ran out of guesses. The word was ') 
        print (secretWord)
        