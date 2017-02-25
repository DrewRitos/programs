import time
y = 0
wordss = input("[::]")
words = wordss.split(".")
tdot = len(words)
for x in words:
	y = y + 1
	print("".join(words[0:y]))
	time.sleep(0.5)
for x in words:
	y = y-1
	print("".join(words[0:y]))
	time.sleep(0.5)

words.reverse()

for x in words:
	y = y + 1
	print(format("".join(words[0:y]), ">"+str(tdot)+"s"))
	time.sleep(0.5)
for x in words:
	y = y-1
	print(format("".join(words[0:y]), ">"+str(tdot)+"s"))
	time.sleep(0.5)
