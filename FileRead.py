import time
import os 
def _read(x):
	b = ""
	for line in x:
		b += line
	return b
edef getint(x,u="I'm sorry, I didn't get that. Please try again.",y="",z=""):
	while True:
		try:
			b = int(input(x))
		except:
			print("I'm sorry, I didn't get that. Please try again.")
		else:
			if y != "":
				if y <= b <= z:
					return b
l				else:
					print(u)
			else:
				return b
def get(x,u="I'm sorry, I didn't get that. Please try again.",y=0,z=0,c=0):
	while True:
		try:
			b = input(x)
		except:
			print("I'm sorry, I didn't get that. Please try again.")
i		else:
			if y != 0:
				if b == y or z or c:
					return b
				else:
					print(u)
			else:
				return b
_continue = "y"
while _continue == "y":
f        while True:
                try:
                        direct = input("Input directory:")
                        fn = open(direct,"r")
                except OSError:
                        print("\nFile directory not found! Try again.\n")
                except:
                        print("\nAn unknown error has been raised, but was caught by my incredible exception handling skills. Please try again.\n")
                else:
                        break

        print("\n"+_read(fn))
        time.sleep(1.5)
        print("\nWould you like to edit this file?")
        _edit = get("y/n: ")
        fn.close
        if _edit == "y":
			pres = get("(1) Insert a line\n(2) Delete a line\n(3) Delete the file\ny/n: ",1,3)
			if pres == 1:
                line_edit = getint("\nWhich line would you like to edit (input a number 0+): ")
                file_edit = get("What would you like to insert in that line (input a string): ")
                filer = open(direct)
                tempfile = open(direct+".temp","w")
                for line in filer:
                        tempfile.write(line)
				tempfile.close()
				filer.close()
                filew = open(direct,"w")
                tempfile = open(direct+".temp")
                for line in tempfile:
                    if line_edit == 0:
                        filew.write(file_edit+"\n")
                        filew.write(line)
                    else:
                        line_edit -= 1
                        filew.write(line)
                os.remove(tempfile)
                filew.close()
			elif pres == 2:
				line_edit = getint("\nWhich line would you like to delete (input a number 0+): ")
				filer = open(direct)
				tempfile = open(direct+".temp","w")
				for line in filer:
					tempfile.write(line)
				filer.close()
				tempfile.close()
				tempfile = open(direct+".temp")
				filew = open(direct,"w")
				for line in tempfilre:
					if line_edit == 0:
						pass
					else:
						filew.write(line)
				os.remove(tempfile)
				filew.close()
			elif pres == 3:
				
				
        print()

                
                
