# readline is a function that we use to readlines from a text line on by one

# first we write to create a file and insert some lines in it
with open("Chapter 9 (File IO)/multilines.txt", "w") as file:
    file.write("""This is line 1
    This is line 2
    This is line 3
    This is line 4""")

# second we reopen the file to open it in read mode to use readlines function
with open("Chapter 9 (File IO)/multilines.txt", "r") as file:
    readlines = file.readlines()
    print(readlines)
    #output : ['This is line 1\n', '    This is line 2\n', '    This is line 3\n', '    This is line 4']
# it baiscally stores lines of the file into a list as strings 