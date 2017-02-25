import time
sec = 0
while True:
	time.sleep(1)
	sec = sec+1
	min = round(sec/60,3)
	hour = round(min/60,5)
	print ("I've waited for",hour,"hours,",min,"minutes, and",sec,"seconds.")
