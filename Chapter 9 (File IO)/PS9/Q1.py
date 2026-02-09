# write a program to read the content from the poem.txt and find whether if it contains the word "twinkle"
#path to the file = Chapter 9 (File IO)/PS9/poem.txt 
# *could have directly used poem.txt with that would created the file outside the chapter folder and i like things neat and clean

with open("Chapter 9 (File IO)/PS9/poem.txt ") as file:

    poem = file.read()

if "twinkle" in poem :
    print("Twinkle word found inside the poem.txt")

else:
    print("Twinkle word does not found in the poem.txt")
    
    