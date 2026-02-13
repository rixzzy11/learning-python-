#constructor are default methods in a class 
#it is called dundur method which automatically gets called at the time class called
class Anime:
    name = "Death Note"
    genre = "Psychology and Thrill"
    ratings = 8.2

    def __init__(self , name , genre , ratings): #when objects craeted it gets called
        print("Anime class is being initiated.")
        self.name = name
        self.genre = genre
        self.ratings = ratings
    
    def get_info(self):
        print(f"Anime Name : {self.name}\nAnime genre : {self.genre}\nRatings : {self.ratings}")


# deathnote = Anime()
jjk = Anime("Jujutsu Kaisen" , "Action and Jujutsu" , 7.2)
jjk.get_info()
