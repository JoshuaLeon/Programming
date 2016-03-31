# Today we are making cookies

def has_cookie:
	try:
		cookie = open("PinkieCookie.txt", "r")
		cookie.close()
		return True
	except:
		return False
		
def set_cookie(name , email):
	cookie = open("PinkieCookie.txt", "w")
	cookie.write(name + "\n")
	cookie.write(email + "\n")
	cookie.close()
	
def greet():
	try:
		cookie = open("PinkieCookie", "r")
		lines = cookie.readlines()
		name = lines[0]
		email = lines[1]
		print "Welcome %s! Nice to see you again, is your email still %s?" % (name, email)
		cookie.close()
	except:
		print "Welcome new user."
		
def show_instructions():
	print "Hello, please enter your name: "
	name = raw_input()
	print "Now enter your email: "
	email = raw_input()
	return (name, email)
		
def main():
	if has_cookie():
		greet()
	
	name, email = show_instructions()
	set_cookie(name, email)
	
	print "Thank you. Have a nice day %!" % (name)
	
main()