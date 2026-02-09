# closing files after each time opening can be hectic 
# so we open file in a special mode called context manager
# we use statements to open file 

with open("Chapter 9 (File IO)/file3.txt" , "w") as file:
    file.write("We are writing inside the file using with as statement.")

# as soon as we get out of the statement the files get automatically close
# so we dont have to close the file manually
