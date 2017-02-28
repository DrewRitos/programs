from FileRead import getint, get, _read, direct
line_edit = getint("\nWhich line would you like to edit (input a number 0+): ")
file_edit = get("What would you like to insert in that line (input a string): ")
filer = open("C:\\"+direct)
save_file = _read(filer)
filew = open("C:\\"+direct+".new","w")
for line in filer:
    if line_edit == 0:
        filew.write(file_edit+"\n")
    else:
        line_edit -= 1
        filew.write(line)
filer.close()
filew.close()
print("\nBefore:")
print(save_file)
print("\nAfter:")
print(_read(open("C:\\"+direct)))
