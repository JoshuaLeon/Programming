# anagram program to find all the combinations of characters
# to help with scrabble

#Recursion
def ana(beg, end):
	if len(end) == 1:
		return [beg+end]
		
	f = []
	for i in range(len(end)):
		f += [bed+end[i]]
		f += ana(beg+end[i], end[:i]+end[i+1:]
	return f

def anagrams(letters):
	# get all the words for the dictionary
	ditcionary = []
	try:
		dictionary_file("american-english.txt", "rb")
	except:
		print "Dictionary file not found"
		dictionary = None
		
	for line in dictionary_file:
		dictionary.append(line.strip())
		
	real_words = []
	words = ana("", letters)
	print "number of anagrams: ", len(words)
	
	for word in words:
		if len(word) > 1 and (word in dictionary):
			real_words.append(word)
	return real_words

def main():
	print "Enter your tiles: " 
	tiles = raw_input()
	words = anagrams(titles)
	
	for word in words:
		print word
		
main()
	