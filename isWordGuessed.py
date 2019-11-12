def isWordGuessed(secretWord,lettersGuessed):
           
    for letter in secretWord:
        if letter in lettersGuessed:
            return ("true")
        else:
            return ("false")
            
        
       
            