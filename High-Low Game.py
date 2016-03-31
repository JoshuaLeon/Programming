# HIGH LOW GUESSING GAME

#def choose_range(x, y, z)
	#x = raw_input("Choose minimum value for range ")
	#y = raw_input ("Choose a maximum value for range ")	
	
#    range = y - x
	

def show_instructions():
	print "First you will choose a range for me to guess in"
	print "Pick a number in the range set and I will try to guess it."
	print "I can do this is no more than" + " " + "guesses."
	print ""
	print "After each guess, enter:"
	print "0  - if I got it right"
	print "-1 - if I guessed too high"
	print "1  - if I guessed too low"


def take_guess(min, max):
	guess = (min + max) / 2
	keep_asking = 1
	while keep_asking == 1:
		print "Is your number ", guess, "?"
		response = raw_input("Was I right? (1, -1, 0): ")
		if response == '0':
			print "AHAHAHAHAHA I WIN!"
			keep_asking = 0
		elif response == '-1':
			print "I have failed you, I will guess lower."
			keep_asking = 0
		elif response == '1':
			print "I have not done as I promised, I will go higher."
			keep_asking = 0
		elif response == '6':
			print "The answer is always time."
		else:
			print "I have won, you're an idiot."
			print "Fine, I will help you, here are the instructions again:"
			show_instructions()
	print ""
	return response, guess

def main():
	show_instructions()
	low = 1
	high = 1000
	guesses = 0
	while high > low:
		response, guess = take_guess(low, high)
		guesses += 1
		if response == '0':
			high = 0
			low = 0
		elif response == '-1':
			high = guess - 1
		elif response == '1':
			low = guess + 1
	if high == low:
		print guess
	print "I was able to do the task in",guesses,"guesses."

main()