#Just to warn you, this is the messiest code I've ever made in my life.
#I can barely understand it myself, so my explanations and comments might be lacking.
#I'm importing time so I can make cool dramatic delays. It's pointless, but cool.
#It kinda gives the feeling like the computer is thinking.
import time
n = 12
#Initial price
Ao = float(input("What is the sticker price of the car?"))
#Interest rate
rr = float(input("What percent rate did the banks give you?"))
#Time to pay it
t = float(input("How many years are you looking to pay it off for?"))
#I convert the rate to a percent in decimal form
r = rr/100
#Multiply the rate and payments per year and save as a variable
rn = r/n
#Multiply payments per year and years to pay and save as an integer
nt = int(n*t)
#I seperated all of the steps in the equation into different variables
step1 = (1+rn)
step2 = step1 ** nt
A = str(Ao*step2)
AUse = float(A)
monthly = AUse/nt
#I printed my calculated information
print("The final price of your car will be $",format(AUse,".2f"),"\nYour monthly payment will be $",format(monthly,".2f")," for the next ",nt," months.", sep = "")
time.sleep(3.5)
print("Okay that's a little too high.")
time.sleep(1.5)
#Ask the user for how much they will pay per month
monpay = float(input("What's the most you're willing to pay a month?"))
#Series of variables to calculate new rate and maximum sticker price for new car
A1 = monpay*nt
step3 = A1/Ao
step4 = step3**(1/nt)
#The unformated new rate
notreallythenewrate = n*step4-n
#The totally formated new rate, made readable now! Praise the lord!
newrate = format(notreallythenewrate*100, ".2f")
step5 = 1+(notreallythenewrate/n)**nt
#This is the new sticker price
Aoo = format(A1/step5,".2f")
time.sleep(1)
#And I print the information here
print("If you want to be able to buy this car within your budget, you would need the bank to offer you an interest rate of ",newrate,"% APR.", sep = "")
time.sleep(2.5)
print("I know you don't want to hear this but if they're really unwilling to budge, then you may have to look into a different car. At the given interest rate of ",rr,"% APR and your maximum monthly payment, the most that you can afford is a car that costs $",Aoo," sticker price.", sep = "")













