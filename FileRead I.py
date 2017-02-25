import time
def _read(x):
	b = ""
	for line in x:
		b += line
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

        print(_read(fn))
        time.sleep(1.5)
        print("\nWould you like to read another file?")
        _continue = input("y/n: ")
