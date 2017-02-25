import time
while True:
	a = float(input("How much time in minutes would you like to wait for?"))
	s = 0
	while True:
		time.sleep(1)
		s = s+1
		mm = s/60
		m = mm/a
		per = float(format(m*100,".1f"))
		print(per,"% completed.", sep = "")
		if per > 100:
			print("Timer completed. Restarting...")
			time.sleep(2)
			break
