'''# write a program to detect if the log file contains python and if
yes the at which line in the log file it contains the python'''

with open("Chapter 9 (File IO)/PS9/log.txt") as file:
    content = file.readlines()
    
lineno = 1
for line in content :
    if "python" in line :
        print("Python found inside the log file.\nline no : " , lineno)
        break
    lineno += 1

else :
    print("Python not found inside the log file")
    