import time
import sys
import random
print ("Welcome to RockPaperScissors!")
time.sleep(1)
c = True
while c is True:
	x = 'Rock','Paper','Scissors'
	d = random.choice(x)
	s = input("<Rock> <Paper> <Scissors>")
	if s == d:
		print ("I chose",d,"and you chose "+s+"!")
		time.sleep(0.5)
		print ("It was a tie!")
		s = input("<Rock> <Paper> <Scissors>")
	if s == "Rock":
		if d == "Paper":
			print ("I chose",d,"and you chose "+s+"! You lose!")
		if d == "Scissors":
			print ("I chose",d,"and you chose "+s+"! You win!")
	if s == "Paper":
		if d == "Rock":
			print ("I chose",d,"and you chose "+s+"! You win!")
		if d == "Scissors":
			print ("I chose",d,"and you chose "+s+"! You lose!")
	if s == "Scissors":
		if d == "Paper":
			print ("I chose",d,"and you chose "+s+"! You win!")
		if d == "Rock":
			print ("I chose",d,"and you chose "+s+"! You win!")
