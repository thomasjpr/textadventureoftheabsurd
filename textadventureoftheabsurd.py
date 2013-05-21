print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1": 
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1": 
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else: 
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	print "4. Pull a goatse!"

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	elif insanity == "4":
		print "You have chosen wisely. Here comes the gimp!"
		print "1. Grab the golf club."
		print "2. Grab the chainsaw."
		print "3. Grab the katana."

		choice = raw_input("> ")

		if choice == "1" or choice == "2":
			print "Oops. Your ass is Zed's now."
		else:
			print "Zed's dead, baby. Zed's dead."

	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
else:
	print "You stumble around and fall on a knife and die. Good job!"