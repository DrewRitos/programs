import sys
#This function will become a represents a single day based on the parameters it is given when it is called. When the user inputs a day, one of the functions lights up and says "It's me!" and prints the right information.
def p(month,day,mon_inp,day_inp,school = 1,weekend = 0,half_day = 0,holiday = ""):
	global d
	if month == mon_inp and day == day_inp:
		d += 1
		if school == 1:
			if half_day == 1:
				print(month, day,"is a half day. You will end school at 12:30.")
			else:
				print(month,day,"is a regular school day.\nGet up... go to school...")
			
		elif school == 0:
			if weekend == 1:
				print(month, day,"is a weekend. You do not have school today!\nGo crazy...")
			elif holiday != "":
				print(month, day,"is "+holiday+" and is a school holiday. You do not have school today!\nEnjoy your day off.")
			else:
				print(month, day,"is not a school day. School hasn't started yet.")

#This function runs the previous function. The difference is this one adds 1 to the variable o for every time it is called. This shortens the code drastically as I don't have to type o += 1 for everytime I call the D function.
def e(month,day,mon_inpp,day_inpp,school = 1,weekend = 0,half_day = 0,holiday = ""):
	global o
	o += 1
	day += o
	p(month,day,mon_inpp,day_inpp,school,weekend,half_day,holiday)


#These just shorten the words
sep = "September"
sepp = "October"
se = "November"
dec = "December"
#These combine to represent the number of days a single D function represents
sd = 0
o = 0
#This turns to 1 when an E function is called so that the program may know if the user has selected an invalid date
d = 0
f = input("Good morning! Would you like to see what kind of school day it is? <y/n>:")
#Sys.exit(0) closes the program if the user says no
if f == "n":
	sys.exit(0)
print()

#while True allows the program to loop and be stopepd whenever it slips into one of the if statements at the bottom that then call the break function
while True:
	mon_inp = input("Month:")
	day_inp = float(input("Day:"))
	print()
	sd = 0
	
	#The following represents September
	e(sep,sd,mon_inp,day_inp,0,0,0)
	e(sep,sd,mon_inp,day_inp,0,0,0)
	e(sep,sd,mon_inp,day_inp,0,0,0)#Weekend technically
	e(sep,sd,mon_inp,day_inp,0,0,0)#Weekend technically
	e(sep,sd,mon_inp,day_inp,0,0,0)
	e(sep,sd,mon_inp,day_inp)
	e(sep,sd,mon_inp,day_inp)
	
	e(sep,sd,mon_inp,day_inp)
	e(sep,sd,mon_inp,day_inp)
	e(sep,sd,mon_inp,day_inp,0,1)
	e(sep,sd,mon_inp,day_inp,0,1)
	e(sep,sd,mon_inp,day_inp)
	e(sep,sd,mon_inp,day_inp,1,0,1)
	e(sep,sd,mon_inp,day_inp)
	
	e(sep,sd,mon_inp,day_inp)
	e(sep,sd,mon_inp,day_inp)
	e(sep,sd,mon_inp,day_inp,0,1)
	e(sep,sd,mon_inp,day_inp,0,1)
	e(sep,sd,mon_inp,day_inp)
	e(sep,sd,mon_inp,day_inp)
	e(sep,sd,mon_inp,day_inp)
	
	e(sep,sd,mon_inp,day_inp,1,0,1)
	e(sep,sd,mon_inp,day_inp)
	e(sep,sd,mon_inp,day_inp,0,1)
	e(sep,sd,mon_inp,day_inp,0,1)
	e(sep,sd,mon_inp,day_inp)
	e(sep,sd,mon_inp,day_inp)
	e(sep,sd,mon_inp,day_inp)
	
	e(sep,sd,mon_inp,day_inp)
	e(sep,sd,mon_inp,day_inp)
	
	#The following represents October
	
	o = 0
	
	e(sepp,sd,mon_inp,day_inp,0,1)
	e(sepp,sd,mon_inp,day_inp,0,1)
	e(sepp,sd,mon_inp,day_inp,0,0,0,"Rosh Hashanah")
	e(sepp,sd,mon_inp,day_inp,0,0,0,"Rosh Hashanah")
	e(sepp,sd,mon_inp,day_inp)
	e(sepp,sd,mon_inp,day_inp)
	e(sepp,sd,mon_inp,day_inp)
	
	e(sepp,sd,mon_inp,day_inp,0,1)
	e(sepp,sd,mon_inp,day_inp,0,1)
	e(sepp,sd,mon_inp,day_inp,0,0,0,"Professional Day")
	e(sepp,sd,mon_inp,day_inp)
	e(sepp,sd,mon_inp,day_inp,0,0,0,"Yom Kippur")
	e(sepp,sd,mon_inp,day_inp)
	e(sepp,sd,mon_inp,day_inp)
	
	e(sepp,sd,mon_inp,day_inp,0,1)
	e(sepp,sd,mon_inp,day_inp,0,1)
	e(sepp,sd,mon_inp,day_inp)
	e(sepp,sd,mon_inp,day_inp)
	e(sepp,sd,mon_inp,day_inp)
	e(sepp,sd,mon_inp,day_inp)
	e(sepp,sd,mon_inp,day_inp)
	
	e(sepp,sd,mon_inp,day_inp,0,1)
	e(sepp,sd,mon_inp,day_inp,0,1)
	e(sepp,sd,mon_inp,day_inp)
	e(sepp,sd,mon_inp,day_inp)
	e(sepp,sd,mon_inp,day_inp)
	e(sepp,sd,mon_inp,day_inp)
	e(sepp,sd,mon_inp,day_inp)
	
	e(sepp,sd,mon_inp,day_inp,0,1)
	e(sepp,sd,mon_inp,day_inp,0,1)
	e(sepp,sd,mon_inp,day_inp)
	
	#The following represents November
	
	o = 0
	
	e(se,sd,mon_inp,day_inp)
	e(se,sd,mon_inp,day_inp)
	e(se,sd,mon_inp,day_inp)
	e(se,sd,mon_inp,day_inp)
	e(se,sd,mon_inp,day_inp,0,1)
	e(se,sd,mon_inp,day_inp,0,1)
	e(se,sd,mon_inp,day_inp)
	
	e(se,sd,mon_inp,day_inp,0,0,0,"Professional Day")
	e(se,sd,mon_inp,day_inp)
	e(se,sd,mon_inp,day_inp,0,0,0,"Teacher's Convention")
	e(se,sd,mon_inp,day_inp,0,0,0,"Teacher's Convention")
	e(se,sd,mon_inp,day_inp,0,1)
	e(se,sd,mon_inp,day_inp,0,1)
	e(se,sd,mon_inp,day_inp)
	
	e(se,sd,mon_inp,day_inp)
	e(se,sd,mon_inp,day_inp)
	e(se,sd,mon_inp,day_inp)
	e(se,sd,mon_inp,day_inp)
	e(se,sd,mon_inp,day_inp,0,1)
	e(se,sd,mon_inp,day_inp,0,1)
	e(se,sd,mon_inp,day_inp)
	
	e(se,sd,mon_inp,day_inp)
	e(se,sd,mon_inp,day_inp,0,0,1)
	e(se,sd,mon_inp,day_inp,0,0,0,"Thanksgiving")
	e(se,sd,mon_inp,day_inp,0,0,0,"Thanksgiving")
	e(se,sd,mon_inp,day_inp,0,1)
	e(se,sd,mon_inp,day_inp,0,1)
	e(se,sd,mon_inp,day_inp)
	
	e(se,sd,mon_inp,day_inp)
	e(se,sd,mon_inp,day_inp)
	
	#The following represents December
	
	o = 0
	
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp)
	
	e(dec,sd,mon_inp,day_inp)
	e(dec,sd,mon_inp,day_inp,0,0,0,"winter break")
	e(dec,sd,mon_inp,day_inp,0,1)
	e(dec,sd,mon_inp,day_inp,0,1)
	e(dec,sd,mon_inp,day_inp,0,0,0,"winter break")
	e(dec,sd,mon_inp,day_inp,0,0,0,"winter break")
	e(dec,sd,mon_inp,day_inp,0,0,0,"winter break")
	
	e(dec,sd,mon_inp,day_inp,0,0,0,"winter break")
	e(dec,sd,mon_inp,day_inp,0,0,0,"winter break")
	e(dec,sd,mon_inp,day_inp,0,0,0,"winter break")
	
	#These are the if statements that allow the program to end if the user wishes, and also catches if the user inputs an invalid date
	if d == 0:
		print("This is not a valid date, please try again.\n")
	else:	
		u = input("\nWould you like to check another day? <y/n>:")
		if u == "n":
			print("\nOkay, have a great day!")
			break
		print()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
