"""a file contains word "donkey" and you have to replace the word with #### """

with open ("Chapter 9 (File IO)/PS9/Donkey.txt" ) as file:
    string = file.read()
    cleaned_string = string.replace("donkey", "####").replace("donkeys", "####")
    
with open ("Chapter 9 (File IO)/PS9/Donkey.txt" , "w") as file:
    file.write(cleaned_string)