# HELLO ANYONE READING THIS (PROBABLY THE FUTURE ME), THIS IS A SIMPLE MADLIB GAME I CREATED :)
# introduction begins
print('Hello there! :) \n it\'s nice to meet you! \n This is a madlib game')
print('you input a word from the part of speech you will be asked')
print('the word will be used to finish a segment of a \'song lyrics\'.')

# initializing some variables
n = input('are you ready to start the game (Y/N): ').lower() # making sure the response is in lowercase
questions = ["type in a noun: ", "type in a pronoun: ", "type in an adjective: ", "type in a verb: ", "type in an adverb: ", "type in a conjuction: "]
count = 0 

# lyrics template
def showLyric():
    print('\n')
    print('----------------------------------------------')
    print(f'Have you seen the state of {questions[1]} body? (Mad)')
    print(f'{questions[5]} I beat it, I ain\'t wearin\' a Jonny (hah)')
    print(f'{questions[0]} when I roll with a geezer (with a geez)')
    print(f'Is it me or the lifestyle {questions[2]}?')
    print(f'{questions[4]}, I don\'t give a shit (nah)')
    print(f'I\'m a rapper now, might as well {questions[3]} in it (live in it)')
    print('----------------------------------------------')
    print('\n')

# starting the game then getting and storing the user's input
if n == 'y' or n == "yes": 
    for question in questions:
        questions[count] = input(question)
        count += 1
    showLyric()
    print('I bet you didn\'t see that coming \n bye for now \n mask up, stay healthy \n emmo cares :)')
else:
    print(':( why na, the game is nice, anyway') # end the game
    print('re-run the game when you are ready. Goodbye!')
