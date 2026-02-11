#write a program to make copy of text file 

with open("Chapter 9 (File IO)/PS9/text.txt") as file:
    read = file.read()
    
with open("Chapter 9 (File IO)/PS9/text_copy.txt" , "w") as file:
    read2 = file.write(read)

