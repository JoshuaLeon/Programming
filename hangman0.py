import random

def get_words():
	word_list = []
	file = open("HangManWords.txt", "r")
	for line in file:
		word_list.append(line.strip())
	return word_list
	# read words.txt file and return
	# all the words in a list
	pass
    
def pick_word(words):
    import random
    return(random.choice(get_words()))
    # Pick a random word from the list of words

def new_game(words):
	# Create a game list that stores all
	# the data for a game
	# game[0] is a list of guessed letters
	# game[1] is the word being guessed
	# game[2] is the number of misses
    guessed_letters = []
    word = pick_word(words)
    misses = 0
    game = [ guessed_letters, word, misses ]
    return game

def is_word_guessed(game):
    for i in game[1]:
    	if i not in game[0]:
    		return False
    return True
    # return True if the word has been guessed (all letters in the word have been guessed)
    # return False otherwise

def is_game_over(game):
    if game[2] == 6 or is_word_guessed(game):
    	return True
    else:
    	return False
    # return True if too many guesses (6 or more),
    # or word has been guessed.
    

def guess_letter(game, letter):
    	game[0].append
    	if letter not in game[1]:
    		game[2] += 1
    	return game
    # add letter to guessed letters list
    # add 1 to misses if letter not in word
    # return the updated game list
    

def display_picture(game):
	# display the man being hanged
    misses = game[2]
    if misses > 0:
        print " O "
        
    if misses == 2:
        print " | "
    elif misses == 3:
        print "/| "
    elif misses >= 4:
        print "/|\\"

    if misses == 5:
        print "/  "
    elif misses >= 6:
        print "/ \\"
    return


def display_word(game):
    hidden = ''
    for i in game[1]:
    	if i in game[0]:
    		hidden += i + " "
    	else:
    		hidden += '_ '
    print hidden
    return

def display_guessed_letters(game):
    print game[0]
    # print the guessed letters list

def display_status(game):
    display_picture(game)
    print
    display_word(game)
    print
    display_guessed_letters(game)
    print
    print
    return

def main():
    words = get_words() #get long list of words
    game = new_game(words) #get a list with the game data  list, string, int
    display_status(game)
    while not is_game_over(game):
        guess = raw_input("next guess? ")
        guess = guess.strip()
        if len(guess) > 0:
            guess = guess.lower()
            game = guess_letter(game, guess[0])
        display_status(game)

    if not is_word_guessed(game):
        print "The word is:", game[1]
        print ""
        
    return

if __name__ == "__main__":
    main()