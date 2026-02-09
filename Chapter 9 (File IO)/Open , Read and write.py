# file input output is used to interact with system files
# we create files , read and write on it on two types of files first text files and second binary

#to open a file we use open() function . it takes two arguments first is file name and second open mode

file = open("Chapter 9 (File IO)/Text.txt" , "r") # default open mode is read so even if we dont use "r" it automatically open it in read mode
text = file.read()
print(text)
file.close()

#if we open a file in write mode it automatically creates a file and we can insert data in it
file = open("Chapter 9 (File IO)/file2.txt" , "w")
text = file.write("Hello from a python code , we are writing data in the file.")
file.close()

#it is important to close the file after using it otherwise we loss the data , memory leak or file lock may happen