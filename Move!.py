import sys
import time
import random
def fformat(e,r):
	return e+"\n"*r
def u(e,r,t=" "):
	if x == e:
		if y == r:
			return "o"
		else:
			return t
	else:
		return t
def i(e,r):
	if x == e:
		if y == r:
			return 1
		else:
			return 0
	else:
		return 0
have_sword = 0
lives = 3
lines = 0
x = 1
y = 1
while True:
	while True:
		lines = 28
		z = input("Go:")
		if z == "right":
			x = x+1
		if z == "left":
			x = x-1
		if z == "up":
			y = y+1
		if z == "down":
			y = y-1
		a1 = u(1,2)
		q1 = i(1,2)
		a2 = u(2,2)
		a3 = u(3,2)
		a4 = u(4,2)
		b1 = u(1,1)
		b2 = u(2,1)
		b3 = u(3,1)
		b4 = u(4,1)
		c1 = u(1,0)
		c2 = u(2,0)
		c3 = u(3,0)
		c4 = u(4,0)
		d1 = u(1,-1)
		d2 = u(2,-1)
		d3 = u(3,-1)
		d4 = u(4,-1)
		q = q1
		if q == 1:
			break
		print("\n")
		print(a1,"|",a2,"|",a3,"|",a4, sep = "")
		print(b1,"|",b2,"|",b3,"|",b4, sep = "")
		print(c1,"|",c2,"|",c3,"|",c4, sep = "")
		print(d1,"|",d2,"|",d3,"|",d4, sep = "")
		lines = lines-7
		if have_sword == 1:
			lines = lines-1
		print("\n"*lines)
		if have_sword == 1:
			print("Sword: x",have_sword, sep = "")
		print("*"*lives," lives left", sep = "")
	if q1 == 1:
		lines = lines-2
		print("\n")
		print(fformat("You found a sword!", lines))
		have_sword = 1
		q1 = 0
		






