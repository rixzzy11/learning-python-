# write a program to to find if the two files are idenctical or not 

with open("Chapter 9 (File IO)/PS9/text.txt") as file:
    content1 = file.read()

with open("Chapter 9 (File IO)/PS9/poem.txt") as file:
    content2 = file.read()

if content1 == content2 :
    print("Both files are identical.")

else:
    print("Files has different content.")