import time
import FileWrite
def _read(x):
	b = ""
	for line in x:
		b += line
	return b
def getint(x,u="I'm sorry, I didn't get that. Please try again.",y="",z=""):
	while True:
		try:
			b = int(input(x))
		except:
			print("I'm sorry, I didn't get that. Please try again.")
		else:
			if y != "":
				if y <= b <= z:
					return b
				else:
					print(u)
			else:
				return b
def get(x,u="I'm sorry, I didn't get that. Please try again.",y=0,z=0,c=0):
	while True:
		try:
			b = input(x)
		except:
			print("I'm sorry, I didn't get that. Please try again.")
		else:
			if y != 0:
				if b == y or z or c:
					return b
				else:
					print(u)
			else:
				return b
_continue = "y"
while _continue == "y":
        while True:
                try:
                        direct = input("C:\\")
                        fn = open("C:\\"+direct,"r")
                except OSError:
                        print("\nFile directory not found! Try again.\n")
                except:
                        print("\nAn unknown error has been raised, but was caught by my incredible exception handling skills. Please try again.\n")
                else:
                        break

        print("\n"+_read(fn))
        time.sleep(1.5)
        print("\nWould you like to edit this file?")
        _edit = input("y/n: ")
        fn.close
        if _edit == "y":
                line_edit = getint("\nWhich line would you like to edit (input a number 0+): ")
                file_edit = get("What would you like to insert in that line (input a string): ")
                filer = open("C:\\"+direct)
                tempfile = open("C:\\"+direct+".temp","w")
                for line in filer:
                        tempfile.write(line)
                filew = open("C:\\"+direct,"w")
                tempfile.close()
                tempfile = open("C:\\"+direct+".temp")
                for line in tempfile:
                    if line_edit == 0:
                        filew.write(file_edit+"\n")
                        filew.write(line)
                    else:
                        line_edit -= 1
                        filew.write(line)
                tempfile.close()
                filew.close()
        print()

                
                
