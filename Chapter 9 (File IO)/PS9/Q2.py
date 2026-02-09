"""write a program to check if the the function returning a score
is grater than previous score which is stored in a txt file to save 
the high score only and only new greater score than prevously stored
score in txt file will be saved in txt file"""

import random
def game_score():   
    return random.randint(1 , 1000) #returns a random value

current_score = game_score() 
print("Your score is ",current_score)  #random value is the current score

with open("Chapter 9 (File IO)/PS9/Hi-score.txt") as file:
    Highscore = file.read() #checking old high score and assigning it to the Highscore
    #if high score dosent exist we will set it to 0
    if(Highscore != ''):          
        Highscore = int(Highscore)
    else:   
        Highscore = 0
        
    print("High score is ",Highscore) #old high score

    if(current_score > Highscore): #if greater score is found store it to file
        with open("Chapter 9 (File IO)/PS9/Hi-score.txt" , "w") as file:
            file.write(str(current_score))
            print("New High-score ",current_score)   
    


