# Mad Lib Game
def lib():
	a = raw_input("Adjective ")
	b = raw_input("Adjective ")
	c = raw_input("Type of Bird ")
	d = raw_input("Room in a house ")
	e = raw_input("Verb [past tense]: ")
	f = raw_input("verb ")
	g = raw_input("Relative name " )
	h = raw_input("Noun ")
	i = raw_input("A liquid ")
	j = raw_input("verb ending in -ing ")
	k = raw_input("part of the body (plural): ")
	l = raw_input("plural noun ")
	m = raw_input("verb ending in -ing ")
	n = raw_input("noun ")
	print "It was a " + a + " cold November day. I woke up to " +\
		b + " the smell of " + c + " roasting in the " + d + " downstairs. I " +\
		e + " down the stairs to see if I could help " +\
		f + ' the dinner. My mom said, "See if ' + g + " needs a fresh " +\
		h + '." So I carried a tray of glasses full of ' + i + " into the " +\
		j + " room. When I got there, I couldn't beleive my " +\
		k + "! There were " + l + " " + m + " on the " + n + "! "                            
def main():
	question = raw_input("Do you want to play? ")
	if question == 'y' or 'Y' or 'YES' or 'yes' or 'Yes':
		lib()
		main()
	else:
		print "Goodbye"
		
main()