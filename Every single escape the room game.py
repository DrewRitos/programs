import time
import sys

def printt(x,y):
	print(x, end = "")
	time.sleep(y)
def ts(x):
	time.sleep(x)
def round_up(a,b):
	if round(a/b,0) < a/b:
		o = int(round(a/b,0)+1)
		return o
	o = int(round(a/b,0))
	return o
def get_lines(q):
	oo = round_up(int(len(q)),78)
	return oo
def prints(x,y,z=0):
	time.sleep(z)
	print(x)
	time.sleep(y)
def printy(x,y=0):
	z = 28-get_lines(x)
	print("\n"*y)
	print(x)
	print("\n"*z)
#X = what to print, Y = delay after message, Z = delay before message, V = how many spaces to print before message
def printys(x,y,z=0,v=0):
	m = 28-get_lines(x)
	print("\n"*v)
	time.sleep(z)
	print(x)
	print("\n"*m)
	time.sleep(y)
def inputys(x,y,z=0,v=40):
	n = 28-get_lines(x)
	print("\n"*v)
	time.sleep(z)
	return input(x)
	print("\n"*n)
	time.sleep(y)

printys("Alright.",1)
printys("Is this working?",2)
printys("Yeah?",1)
printys("Okay hey. Listen. You're gonna have this wiped from your memory in a few seconds, but you're going to be put in a game. Because that's what this is. A game. I just had to set some stuff up before I could start the game.",7.5)
printys("Hold on I'm getting a call from another player, I'll start the game for you.",4)
q1 = inputys("""You've been invited to start game: 5437e453b901a566, would you like to start it? 
<y> <n>""",1.5)
if q1 == "n":
	printys("Error: OS not found, shutting down...",3,1.5)
	sys.exit(0)
elif q1 == "y":
	pass
else:
	printys("Error: OS not found, shutting down...",3,1.5)
	sys.exit(0)
printys("You notice you are in a small room. It's dark, but you can just barely see.",2.5)
printys("Maybe try looking around...",2.5)
room_match = 1
room_candle = 1
room_key = 1
room_stool = 1
have_candle = 0
have_match = 0
have_key = 0
have_stool = 0
dy = 0
dx = 0
while True:
	direction = inputys("Left <l> Right <r> Up <u> Down <d> Stay <s>",1.5)
	if direction == "s":
		pass
	if direction == "l":
		dx = dx - 1
	if direction == "r":
		dx = dx + 1
	if direction == "u":
		dy = dy + 1
	if direction == "d":
		dy = dy - 1
	if dx == -1:
		if dy == -1:
			printys("You see the carpet underneath you.",2.5)
		if dy == 0:
			printys("You see a small wooden workbench.",2)
			printys("On top there is a candle, a deck of cards, and a lockbox.",2)
			printys("Interact with..",1.5)
			q2 = inputys("The candle <1> The deck of cards <2> The lockbox <3>",1)
			if q2 == "1":
				if have_match == 0:
					printys("You have no use for the candle right now.",2)
				if have_match == 1:
					printys("You take use the match to light the candle. You can see clearly now.",2.75)
					have_match = 0
					have_candle = 1
					room_candle = 0
			if q2 == "2":
				printys("You pick up the deck of cards and shuffle through it.",1.5)
				if have_candle == 0:
					printys("It's too dark to see anything on the cards.",2.1)
				if have_candle == 1:
					printys("You notice that a few of the cards have numbers on them:",2.5)
					printys("4:2, 2:8, 1:3, 3:6",10)
					printys("How strange.",1.5)
			if q2 == "3":
				printys("It's locked with a padlock.",1.5)
				printys("It reads...",1.5)
				q6 = inputys("Input 4 digit PIN:",1)
				if q6 == "3862":
					if room_key == 1:	
						printys("The lockbox clicks open, and inside there is a small silver key. You take it.",3)
						have_key = 1
						room_key = 0
					elif room_key == 0:
						printys("The lockbox clicks open, but there is nothing inside.",2.5)
				else:
						printys("That was the incorrect code.",1.25)
		if dy == 1:
			printys("On the ceiling, there is a small hook holding a key.",2.5)
			q3 = inputys("Reach for the key <1> Do nothing <2>",1)
			if q3 == "1":
				if have_stool == 0:	
					printys("You reach up as high as you can but the key is just out of your reach.",3)
					printys("If only you had something to boost your hight a little...",3)
				if have_stool == 1:
					printys("You place the stool on the floor and get up onto it.",2)
					printys("The boost in hight allows you to easily grab the key.",2)
					printys("Upon closer inspection, the key reads: EXIT.",2.5)
					have_key = 1
					room_key = 0
			if q3 == "2":
				printys("You do nothing.",2)
	if dx == 0:
		if dy == -1:
			if room_match == 1:
					printys("You notice a single match stuck in the carpeting.",2.5)
					printys("Do you...",1.25)
					q4 = inputys("Take the match <1> Leave it <2>",1)
					if q4 == "1":
						printys("You reach down and pick up the match. Huh. That was simple.",2.5)
						have_match = 1
						room_match = 0
					if q4 == "2":
						printys("You leave the match alone.",1.5)
			if room_match == 0:
				if have_candle == 1:
					printys("You shine the candlelight at the floor, but see nothing.",3)
				elif have_candle == 0:
					printys("You look at the dark floor, and see nothing.",2.5)
		elif dy == 0:
			printys("In front of you you see a stout metal door with no window.",2)
			printys("The door has a lock on it that requires a key.",1.5)
			if have_key == 1:
				printys("You push the key into the lock and turn it.",1.5)
				printys("You hear a satisfying clicking noise, and you push the door open.",3)
				printt("Y",1)
				printt("O",1)
				printt("U ",1)
				printt("W",1)
				printt("I",1)
				printt("N",1)
		elif dy == 1:
			printys("You see the ceiling. Nothing here.",2)
	if dx == 1:
		if dy == -1:
			if room_stool == 1:
				printys("You see a stool on the floor.")
				q7 = inputys("Pick it up? <y> <n>",1)
				if q7 == "y":
					printys("You pick up the stool.")
					have_stool = 1
					room_stool = 0
				if q7 == "n":
					printys("You decide not to pick up the stool.",2)
			else:
				printys("There's nothing but the carpet on the floor.",2)
		elif dy == 0:
			if have_candle == 1:
				printys("You shine the candlelight onto the wall, revealing a magnificent painting of a distinguished looking man in a tuxedo.",5)
			if have_candle == 0:
				printys("The wall is too dark to see.",1.5)
		elif dy == 1:
			printys("You see the ceiling. Nothing here.")
